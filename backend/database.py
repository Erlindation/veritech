"""
database.py
-----------
SQLAlchemy engine and session configuration.
All models import Base from here to register their tables.
"""

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

# Each request gets its own session, closed when done.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All models inherit from Base so SQLAlchemy can create their tables.
Base = declarative_base()


def get_db():
    """
    FastAPI dependency that provides a DB session per request.
    Guarantees the session is closed even if an error occurs.

    Usage in a router:
        db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
