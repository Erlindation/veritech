"""
main.py
-------
FastAPI application entry point.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine, Base

# Create all tables on startup (skipped if DB is unreachable)
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"WARNING: Could not create tables: {e}")

app = FastAPI(
    title="VeriTech API",
    description="Fact-checking platform — verify claims against real sources.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "VeriTech API is running"}
