# Endpoints de autenticación. Aquí viven las rutas HTTP — nada más.
# La lógica real (hashing, tokens) está en services/auth.py.
# La separación es intencional: si mañana cambio cómo funciona el JWT,
# no tengo que tocar los endpoints.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.user import User
from backend.schemas.users import UserCreate, UserLogin, UserResponse
from backend.services.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Primero compruebo que el email no existe ya — si existe, paro aquí.
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este email ya está registrado."
        )

    new_user = User(
        email=user_data.email,
        hashed_password=hash_password(user_data.password),  # nunca guardo la contraseña en texto plano
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # refresco para obtener el id y created_at que puso la BD
    return new_user


@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.email).first()

    # El mismo error tanto si el email no existe como si la contraseña es incorrecta.
    # No quiero dar pistas sobre qué falló exactamente.
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
