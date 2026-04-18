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
├── main.py              # Punto de entrada FastAPI, arranque del servidor
├── database.py          # Conexión SQLAlchemy + fábrica de sesiones
├── models/
│   └── user.py          # Modelo ORM — tabla users en PostgreSQL
├── schemas/
│   └── users.py         # Validación de datos de entrada y salida (Pydantic)
├── routers/
│   └── auth.py          # POST /auth/register, POST /auth/login
└── services/
    └── auth.py          # Hashing bcrypt + generación/verificación JWT
```

---

## Estado actual

### Completado
- Conexión verificada a PostgreSQL en la nube (Supabase) mediante Transaction Pooler
- Servidor FastAPI arrancando con health check funcional en `GET /`
- Modelo ORM `User` con SQLAlchemy (tabla `users`: email, contraseña hasheada, estado, fecha de creación)
- Schemas Pydantic para registro, login y respuesta — contraseña nunca expuesta en respuestas
- Lógica de autenticación completa: hashing bcrypt y tokens JWT con expiración
- `POST /auth/register` — registro de usuarios con validación de email duplicado
- `POST /auth/login` — verificación de credenciales y emisión de token Bearer
- Documentación interactiva Swagger disponible en `/docs`

### En desarrollo
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
