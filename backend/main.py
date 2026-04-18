# Punto de entrada de la aplicación. Aquí arranca todo.
# Para lanzarlo: uvicorn backend.main:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine, Base
from backend.routers import auth, claims

# Intenta crear las tablas al arrancar. Si la BD no responde, avisa pero no peta.
# Cuando añada más modelos (claims, etc.) se crearán aquí también automáticamente.
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Aviso: no se pudieron crear las tablas — {e}")

app = FastAPI(
    title="VeriTech API",
    description="Plataforma de verificación de afirmaciones factuales.",
    version="0.1.0",
)

# CORS abierto por ahora para no tener problemas desde el navegador en local.
# Cuando haya frontend real, aquí se pone solo su dominio.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(claims.router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "VeriTech API funcionando"}
