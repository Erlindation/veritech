# Endpoints para gestionar afirmaciones.
# Solo usuarios autenticados pueden enviar y consultar claims — de ahí el token JWT.

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.claim import Claim
from backend.schemas.claims import ClaimCreate, ClaimUpdate, ClaimResponse
from backend.services.auth import decode_access_token
from backend.services.fact_check import check_claim
from backend.models.user import User

router = APIRouter(prefix="/claims", tags=["Afirmaciones"])

# HTTPBearer se encarga de leer el token del header Authorization: Bearer <token>
bearer_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
):
    # Decodifico el token para saber quién hace la petición.
    # Si el token es inválido o ha expirado, paro aquí.
    email = decode_access_token(credentials.credentials)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado.",
        )
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user


@router.post("/", response_model=ClaimResponse, status_code=status.HTTP_201_CREATED)
def create_claim(
    claim_data: ClaimCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Consulto la API antes de guardar — así el veredicto queda en la BD desde el principio.
    verdict = check_claim(claim_data.text)

    new_claim = Claim(
        user_id=current_user.id,
        text=claim_data.text,
        verdict=verdict,
    )
    db.add(new_claim)
    db.commit()
    db.refresh(new_claim)
    return new_claim


@router.get("/", response_model=list[ClaimResponse])
def get_my_claims(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    limit: int = 20,
    offset: int = 0,
):
    # Devuelve solo las afirmaciones del usuario autenticado — no las de otros.
    # Sin limit esto devolvería todo de golpe si hay miles de claims.
    return (
        db.query(Claim)
        .filter(Claim.user_id == current_user.id)
        .offset(offset)
        .limit(limit)
        .all()
    )


@router.get("/{claim_id}", response_model=ClaimResponse)
def get_claim(
    claim_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    claim = db.query(Claim).filter(Claim.id == claim_id, Claim.user_id == current_user.id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Afirmación no encontrada.")
    return claim


@router.put("/{claim_id}", response_model=ClaimResponse)
def update_claim(
    claim_id: int,
    claim_data: ClaimUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    claim = db.query(Claim).filter(Claim.id == claim_id, Claim.user_id == current_user.id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Afirmación no encontrada.")
    claim.text = claim_data.text
    claim.verdict = check_claim(claim_data.text)
    db.commit()
    db.refresh(claim)
    return claim


@router.delete("/{claim_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_claim(
    claim_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    claim = db.query(Claim).filter(Claim.id == claim_id, Claim.user_id == current_user.id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Afirmación no encontrada.")
    db.delete(claim)
    db.commit()
