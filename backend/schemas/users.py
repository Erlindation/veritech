# Pydantic es la librería que valida los datos que entran y salen de la API.
# Cada clase aquí define la "forma" de los datos — qué campos existen y qué tipo tienen.
# Si alguien manda datos incorrectos, Pydantic los rechaza automáticamente antes de
# que lleguen a la base de datos.
from pydantic import BaseModel, EmailStr, ConfigDict


# Datos que el usuario manda al registrarse.
# EmailStr valida que el email tenga formato correcto (contiene @, dominio, etc.).
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Datos que el usuario manda al iniciar sesión.
# Es igual a UserCreate, pero se separa para que en el futuro se pueda cambiar
# uno sin afectar al otro.
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Datos que la API devuelve sobre un usuario.
# NUNCA incluye la contraseña — ni siquiera el hash.
# from_attributes=True permite que Pydantic lea directamente
# desde un objeto de SQLAlchemy (en vez de un diccionario).
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    is_active: bool

