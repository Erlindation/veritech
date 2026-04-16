# Configuración de la conexión a la base de datos.
# Todo lo que tenga que ver con sesiones y el motor de SQLAlchemy vive aquí.
# Los modelos importan Base desde aquí para que SQLAlchemy sepa qué tablas crear.

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")

engine = create_engine(DATABASE_URL)

# Cada petición HTTP abre su propia sesión y la cierra al terminar.
# autocommit=False significa que tengo que hacer db.commit() manualmente — así controlo cuándo se guarda.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base es la clase madre de todos mis modelos.
# Cuando hago class User(Base), SQLAlchemy sabe que tiene que crear una tabla para eso.
Base = declarative_base()


def get_db():
    # FastAPI usa esto como dependencia en los endpoints.
    # Abre la sesión, la cede al endpoint, y la cierra siempre — aunque haya un error.
    # Se usa así en un router: db: Session = Depends(get_db)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
