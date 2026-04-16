# Toda la lógica de autenticación está aquí: hashing de contraseñas y tokens JWT.
# Este archivo no sabe nada de HTTP ni de FastAPI — solo hace cálculos.
# Los endpoints en routers/auth.py llaman a estas funciones.

from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
import os

SECRET_KEY = os.getenv("SECRET_KEY", "cambia_esto_en_produccion")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # el token dura 24 horas

# bcrypt es el estándar actual para hashear contraseñas.
# deprecated="auto" marca automáticamente los hashes viejos como obsoletos si algún día cambio el algoritmo.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    # Convierte la contraseña en texto plano a un hash. Lo que se guarda en la BD es esto.
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Comprueba si la contraseña que manda el usuario coincide con el hash guardado.
    # bcrypt rehashea internamente para comparar — yo no tengo que hacer nada más.
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    # Genera un token JWT firmado con el email del usuario como identificador ("sub").
    # El frontend guarda este token y lo manda en cada petición para demostrar quién es.
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> Optional[str]:
    # Verifica que el token es válido y no ha expirado.
    # Devuelve el email del usuario si todo va bien, None si algo falla.
    # Cuando implemente rutas protegidas, usaré esto para saber quién hace la petición.
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None
