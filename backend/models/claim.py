# Tabla donde se guardan las afirmaciones que envían los usuarios.
# Cada claim pertenece a un usuario — de ahí el ForeignKey a users.id.

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from backend.database import Base


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(String, nullable=False)
    verdict = Column(String, nullable=True)
    source = Column(String, nullable=True)  # URL del artículo de fact-check que emite el veredicto
    created_at = Column(DateTime(timezone=True), server_default=func.now())
