# Schemas para las afirmaciones — qué manda el usuario y qué devuelve la API.

from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


# Lo que manda el usuario: solo el texto de la afirmación.
class ClaimCreate(BaseModel):
    text: str


# Para actualizar un claim — solo el texto es modificable.
class ClaimUpdate(BaseModel):
    text: str


# Lo que devuelve la API al crear o consultar una afirmación.
# El veredicto puede ser None si todavía no se ha comprobado.
class ClaimResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    text: str
    verdict: Optional[str]
    created_at: datetime
