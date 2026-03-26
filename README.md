# VeriTech

> Aplicación web para verificación de información online basada en evidencias.

Autor: Erlinda Canillas Sánchez.

## ¿Qué es VeriTech?

VeriTech permite a usuarios registrados introducir afirmaciones factuales en lenguaje natural y recibir un veredicto estructurado (*Verificable*, *Engañoso* o *No comprobable*) respaldado por evidencias obtenidas de la Google Fact Check Tools API. Todas las consultas se almacenan en PostgreSQL para consulta posterior.

---

## Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Backend | Python 3.13 + FastAPI |
| Base de datos | PostgreSQL (Supabase) |
| ORM | SQLAlchemy |
| Autenticación | JWT (python-jose + bcrypt) |
| Servidor | Uvicorn |
| Testing API | Swagger UI (integrado en FastAPI) |

---

## Estructura del proyecto

```
backend/
├── main.py              # Punto de entrada FastAPI
├── database.py          # Conexión SQLAlchemy + sesiones
├── models/
│   └── user.py          # Modelo ORM tabla users
├── routers/             # Endpoints (en desarrollo)
└── services/            # Lógica de negocio (en desarrollo)
```

---

## Estado actual (entrega parcial — marzo 2026)

### Completado
- Conexión a base de datos PostgreSQL (Supabase) verificada
- Modelo ORM `User` definido con SQLAlchemy
- Punto de entrada FastAPI con health check en `GET /`
- Todas las dependencias instaladas y documentadas en `requirements.txt`
- Entorno virtual configurado

### En desarrollo
- `POST /auth/register` y `POST /auth/login` — registro e inicio de sesión con JWT
- `POST /claims` y `GET /claims` — envío y consulta de afirmaciones
- Integración con Google Fact Check Tools API
- Frontend

---

## Instalación local

### Requisitos previos

| Herramienta | Versión mínima |
|-------------|---------------|
| Python | 3.11+ |
| Git | cualquiera |
| VS Code | cualquiera |

### Pasos

```bash
git clone https://github.com/Erlindation/veritech.git
cd veritech
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.template .env         # Rellenar con credenciales propias
uvicorn backend.main:app --reload
```

Accede a la documentación interactiva en: `http://localhost:8000/docs`
