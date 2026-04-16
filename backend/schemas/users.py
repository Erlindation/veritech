# Pydantic valida los datos que entran y salen de la API.
# Si alguien manda un email sin @ o le falta un campo, Pydantic lo rechaza
# antes de que llegue a la base de datos — sin que yo tenga que escribir esas comprobaciones.

from pydantic import BaseModel, EmailStr, ConfigDict


# Lo que manda el usuario al registrarse.
# EmailStr comprueba que el email tiene formato válido (no solo que sea un string cualquiera).
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Lo que manda al hacer login. Por ahora igual que UserCreate,
# pero los separo por si en el futuro quiero tratarlos distinto.
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Lo que devuelve la API sobre un usuario.
# La contraseña NO aparece aquí — ni el hash. Nunca se devuelve.
# from_attributes=True le dice a Pydantic que puede leer directamente
# desde el objeto de SQLAlchemy, no solo desde un diccionario.
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    is_active: bool
