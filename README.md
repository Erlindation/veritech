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
| API externa | Google Fact Check Tools API |
| Frontend | HTML + CSS + JavaScript vanilla |
| Testing API | Swagger UI (integrado en FastAPI) |

---

## Estructura del proyecto

```
backend/
├── main.py              # Punto de entrada FastAPI, arranque del servidor
├── database.py          # Conexión SQLAlchemy + fábrica de sesiones
├── models/
│   ├── user.py          # Tabla users — datos del usuario registrado
│   └── claim.py         # Tabla claims — afirmaciones y veredictos
├── schemas/
│   ├── users.py         # Validación de datos de usuario (entrada y salida)
│   └── claims.py        # Validación de afirmaciones
├── routers/
│   ├── auth.py          # POST /auth/register, POST /auth/login
│   └── claims.py        # CRUD completo de afirmaciones
└── services/
    ├── auth.py          # Hashing bcrypt + generación/verificación JWT
    └── fact_check.py    # Integración con Google Fact Check Tools API

frontend/
├── index.html           # Pantalla de login y registro
├── claims.html          # Dashboard — lista de afirmaciones y CRUD
├── api.js               # Llamadas a la API REST + gestión del token JWT
└── style.css            # Estilos
```

---

## Endpoints disponibles

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| GET | `/` | No | Health check |
| POST | `/auth/register` | No | Registro de usuario |
| POST | `/auth/login` | No | Login — devuelve token JWT |
| POST | `/auth/reset-password` | No | Cambia la contraseña de una cuenta existente |
| POST | `/claims/` | JWT | Envía una afirmación y recibe veredicto |
| GET | `/claims/` | JWT | Lista las afirmaciones del usuario (paginado) |
| GET | `/claims/{id}` | JWT | Devuelve una afirmación concreta |
| PUT | `/claims/{id}` | JWT | Actualiza el texto y obtiene nuevo veredicto |
| DELETE | `/claims/{id}` | JWT | Elimina una afirmación |

Documentación interactiva completa en `http://localhost:8000/docs` con Swagger

---

## Estado actual

### Completado
- Conexión verificada a PostgreSQL en la nube (Supabase) con RLS habilitado
- Servidor FastAPI arrancando con health check en `GET /`
- Modelo ORM `User` — tabla `users` con email, contraseña hasheada, estado y fecha
- Modelo ORM `Claim` — tabla `claims` con texto, veredicto y referencia al usuario
- Schemas Pydantic con validación: email con formato, contraseña mínimo 8 caracteres, contraseña nunca expuesta en respuestas
- Autenticación completa: hashing bcrypt + tokens JWT Bearer con expiración de 24h
- `POST /auth/register` — rechaza emails duplicados y contraseñas débiles
- `POST /auth/login` — error genérico identificado y corregido (no se sabe si el email existe)
- CRUD completo sobre `claims` operativo y probado en Swagger
- `POST /auth/reset-password` — permite cambiar la contraseña de una cuenta existente
- Campo `source` en claims — URL del artículo de fact-check que emite el veredicto
- Frontend funcional: login, registro, listado de afirmaciones, crear, editar inline y eliminar
- Veredicto con etiquetas de color (verde / rojo / gris según resultado)
- Columna Fuente con enlace al artículo original cuando la API lo devuelve

### Pendiente / mejoras posibles
- Adaptación del diseño a pantallas pequeñas
- Clasificación propia del veredicto en lugar de mostrar el texto literal que devuelve Google
- Filtrado y búsqueda de afirmaciones en el dashboard
- Historial exportable (CSV o PDF)

---

## Limitaciones conocidas

**Precisión del veredicto**
La Google Fact Check Tools API no evalúa afirmaciones directamente. Busca fact-checks ya publicados por terceros (Snopes, Maldita, Reuters, etc.) que se parezcan al texto enviado, y devuelve el veredicto que ese fact-checker asignó a su propia formulación. Esto implica dos situaciones habituales:

- Si la afirmación enviada no tiene un fact-check previo exacto, la API devuelve "No comprobable" aunque la afirmación sea verificable.
- Si existe un fact-check sobre una afirmación relacionada pero formulada de forma distinta (por ejemplo, en sentido contrario), el veredicto devuelto puede no corresponderse con la afirmación original.

Esta limitación se informa al usuario en la interfaz y se contempla como área de mejora futura: sustituir o complementar la API con un modelo de lenguaje que evalúe la afirmación directamente.

---

## Decisiones técnicas relevantes

**Frontend: HTML + CSS + JS vanilla en lugar de React**
La idea inicial era React. Se descartó por tiempo: con el plazo disponible, el coste de configuración y estructura de React no se compensaba con el resultado. HTML + CSS + JS vanilla consume exactamente la misma API REST con `fetch`, produce una demo completamente funcional del CRUD y el código es más directo y explicable en la defensa.

---

## Variables de entorno necesarias

Copia `.env.template` a `.env` y rellena:

| Variable | Descripción |
|----------|-------------|
| `DATABASE_URL` | URL de conexión PostgreSQL (Supabase Transaction Pooler) |
| `SECRET_KEY` | Clave para firmar los tokens JWT — mínimo 32 caracteres |
| `GOOGLE_FACT_CHECK_API_KEY` | Clave de la Google Fact Check Tools API |

-> Credenciales para Google Check Tools API añadida a .env

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

Acceso a la documentación interactiva en: `http://localhost:8000/docs`

Para ver el frontend: `frontend/index.html`  (extensión Live Server de VS Code)
