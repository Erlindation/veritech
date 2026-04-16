# Este archivo define la tabla "users" en la base de datos.
# Cada atributo de la clase es una columna de la tabla.
# SQLAlchemy se encarga de traducir esto a SQL — yo no tengo que escribir CREATE TABLE.

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # nunca se guarda la contraseña en texto plano
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # la BD pone la fecha sola
