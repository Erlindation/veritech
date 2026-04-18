# Changelog – VeriTech
**Erlinda Canillas Sánchez · 2º DAM · UAX FP · 2025–2026**

Este archivo recoge el registro real de trabajo del proyecto, semana a semana.
Se utiliza como base para la planificación real del Plan de Trabajo (comparativa con la planificación inicial).

---

## [Semana 1] – 15/02/2026

### Decisiones tomadas
- Comienzo el proyecto con la idea general definida: plataforma web donde usuarios puedan
  registrarse, iniciar sesión y verificar afirmaciones factuales.
- Las afirmaciones se contrastarán con fuentes obtenidas de APIs públicas y web scraping.
- **Decisión de tecnología principal:** Python como lenguaje de backend.
  Se descarta Java + Spring Boot (recogido en la propuesta inicial) en favor de Python + FastAPI,
  por mayor familiaridad con el ecosistema Python en el entorno laboral actual (Bluetree),
  lo que permite un desarrollo más ágil y una mejor integración con las herramientas
  de análisis de datos utilizadas a diario (pandas, httpx, etc.).
- **Decisión de base de datos:** Se descarta Firebase Authentication en favor de
  PostgreSQL con autenticación JWT propia. PostgreSQL es una solución más robusta,
  relacional y adecuada para garantizar la trazabilidad de evidencias que requiere VeriTech.

### Investigación realizada
- Estudio de APIs públicas disponibles para fact-checking (Google Fact Check Tools API).
- Revisión de herramientas similares: maldita.es, Reuters Fact Check, Google Fact Check Explorer.

### Horas dedicadas
| Actividad | Tiempo |
|-----------|--------|
| Definición de requisitos e idea general | 1h |
| Investigación de APIs y herramientas similares | 0h 30min |
| **Total semana** | **1h 30min** |

---

## [Semana 2] – 22/02/2026

### Añadido
- Creación del proyecto en VS Code.
- Inicialización del repositorio en GitHub.
- Primeros pasos en la estructura de carpetas del proyecto.
- Trabajo en la memoria: ampliación de la sección de Justificación e Introducción.

### Horas dedicadas
| Actividad | Tiempo |
|-----------|--------|
| Configuración del entorno y repositorio Git | 0h 45min |
| Estructura inicial del proyecto | 0h 15min |
| Redacción de memoria (Justificación e Introducción) | 0h 30min |
| **Total semana** | **1h 30min** |

---

## [Semana 3] – 26/02/2026

### Decisiones de diseño técnico
Tras revisar el stack utilizado en Bluetree, se define la arquitectura técnica definitiva del backend:

- **Base de datos:** PostgreSQL
- **Testing de API:** Swagger UI (generado automáticamente por FastAPI)
- **Autenticación:** JWT (JSON Web Tokens) con python-jose y bcrypt
- **Backend:** Python con FastAPI
- **Servidor ASGI:** Uvicorn
- **Entorno:** Virtual environment con `venv`

### Horas dedicadas
| Actividad | Tiempo |
|-----------|--------|
| Definición del stack técnico definitivo | 0h 45min |
| Documentación de decisiones de diseño | 0h 30min |
| **Total semana** | **1h 15min** |

---

## [Semana 4] – 07/03/2026

### Añadido
- Estructura completa de carpetas del proyecto (`backend/`, `routers/`, `services/`, `frontend/`).
- Archivo `requirements.txt` con dependencias pinadas.
- Archivo `.env.template` con variables de entorno necesarias.
- Archivo `.gitignore` configurado para excluir `venv/`, `.env` y `__pycache__/`.
- Virtual environment creado e inicializado con todas las dependencias.
- `database.py`: conexión SQLAlchemy al servidor de base de datos.
- `models.py`: modelos ORM para las tablas `users`, `claims`, `evidence`, `results`.
- `schemas.py`: modelos Pydantic para validación de peticiones y respuestas.
- `auth.py`: lógica JWT (creación y verificación de tokens) y hashing de contraseñas con bcrypt.
- `main.py`: punto de entrada FastAPI con middleware CORS y health check en `/`.
- `routers/auth.py`: endpoints `POST /auth/register` y `POST /auth/login`.
- `routers/claims.py`: endpoints `POST /claims` y `GET /claims`.
- `services/fact_check.py`: módulo de integración con Google Fact Check Tools API.

### Problemas encontrados y resueltos
- **Conflicto con Git:** problema al mover el proyecto entre directorios.
  Solución: reubicación del proyecto en `C:/dev/` y re-subida al repositorio con nombre actualizado
  para poder trabajar en múltiples equipos de forma segura.
- **Decisión de base de datos:** se decide sustituir pgAdmin local por **Supabase**
  (PostgreSQL en la nube) para facilitar el despliegue y poder acceder a la base de datos
  desde distintos equipos sin configuración local adicional.
  Esto simplifica también la sección de Despliegue e Instalación de la memoria.

### Horas dedicadas
| Actividad | Tiempo |
|-----------|--------|
| Estructura de carpetas y archivos de configuración | 1h |
| Modelos ORM y schemas Pydantic | 1h 30min |
| Módulo de autenticación JWT | 1h |
| Routers auth y claims | 1h |
| Servicio Google Fact Check API | 0h 45min |
| Resolución de problemas con Git | 0h 30min |
| Investigación y configuración de Supabase | 0h 45min |
| **Total semana** | **6h 30min** |

---

## [Semana 5] – 26/03/2026

### Contexto
Primera sesión de trabajo tras el período de exámenes. Se retoma el proyecto con el objetivo de consolidar la base del backend y dejar el sistema de autenticación en estado avanzado.

### Problemas encontrados y resueltos
- **Proyecto en OneDrive con espacios y caracteres especiales en la ruta:**
  Git y OneDrive son incompatibles (OneDrive intenta sincronizar `.git/` mientras Git escribe en él, lo que puede corromper el repositorio). Solución: migración del proyecto a `C:\dev\VeriTech`, ruta sin espacios ni tildes.
- **Remote de Git con URL inválida:** el remote `origin` apuntaba a un valor placeholder. Solución: `git remote set-url origin git@github.com:Erlindation/veritech.git`.
- **Conexión a Supabase fallando por DNS:** la URL de conexión directa (`db.xxxx.supabase.co:5432`) no resolvía en la red actual. Solución: cambio a Transaction Pooler (`aws-1-eu-west-1.pooler.supabase.com:6543`) con IPv4 forzado desde el panel de Supabase.
- **Contraseña con caracteres especiales en la URL de conexión:** el símbolo `!` requiere URL-encoding (`%21`) en una cadena de conexión PostgreSQL. Solución temporal: contraseña sin caracteres especiales para el entorno de desarrollo.

### Añadido
- `backend/main.py`: punto de entrada FastAPI con middleware CORS y health check en `GET /`. Las tablas se crean automáticamente al arrancar (`Base.metadata.create_all`).
- `backend/models/user.py`: modelo ORM SQLAlchemy para la tabla `users` (campos: `id`, `email`, `hashed_password`, `is_active`, `created_at`).
- `backend/schemas/users.py`: modelos Pydantic para validación de datos de usuario (`UserCreate`, `UserLogin`, `UserResponse`). Separación explícita entre datos de entrada y datos de respuesta — la contraseña nunca se devuelve.

### Referencia de diseño
La estructura del backend (separación en `models/`, `schemas/`, `routers/`, `services/`), el patrón de sesiones por petición con `get_db()`, y el uso de Pydantic para validar entradas y filtrar salidas están directamente inspirados en la arquitectura de los pipelines ETL y dashboards desarrollados en Bluetree, empresa donde trabajo actualmente. Esta familiaridad con el patrón ha permitido tomar decisiones de diseño con criterio propio y no solo seguir tutoriales.
- README actualizado con estado real del proyecto, estructura de carpetas y pasos de instalación.

### Horas dedicadas
| Actividad | Tiempo |
|-----------|--------|
| Resolución de problemas Git y migración de carpeta | 0h 45min |
| Configuración y depuración de conexión a Supabase | 1h |
| Implementación de `main.py` y modelo `User` | 0h 45min |
| Implementación de schemas Pydantic (`users.py`) | 0h 30min |
| Documentación (README y changelog) | 0h 30min |
| **Total sesión** | **3h 30min** |

---
## [Semana 6] – 16/04/2026

### Añadido
- `backend/services/auth.py`: lógica de autenticación completa — hashing de contraseñas con bcrypt (`hash_password`, `verify_password`) y generación/verificación de tokens JWT (`create_access_token`, `decode_access_token`). El token expira en 24 horas. La clave secreta se lee del `.env`.
- `backend/routers/auth.py`: endpoints de autenticación conectados a la base de datos:
  - `POST /auth/register` — crea un usuario nuevo, devuelve sus datos sin contraseña. Rechaza emails duplicados.
  - `POST /auth/login` — verifica credenciales y devuelve un token JWT Bearer.
- `backend/main.py`: router de autenticación registrado en la aplicación.

### Referencia de diseño
La separación entre `services/` (lógica pura) y `routers/` (endpoints HTTP) sigue el mismo patrón de capas usado en los pipelines de Bluetree, donde la lógica de negocio nunca vive directamente en el punto de entrada.

### Horas dedicadas
| Actividad | Tiempo |
|-----------|--------|
| Implementación de `services/auth.py` (bcrypt + JWT) | 1h |
| Implementación de `routers/auth.py` (register + login) | 1h 15min |
| Conexión del router en `main.py` y pruebas en Swagger | 0h 45min |
| **Total sesión** | **3h** |

---

## [Semana 6 - Segunda sesión] – 18/04/2026

### Añadido
- `backend/models/claim.py`: modelo ORM para la tabla `claims` — guarda el texto de la afirmación, el veredicto (de momento vacío hasta integrar la API externa) y la referencia al usuario que la envió.
- `backend/schemas/claims.py`: schemas Pydantic para afirmaciones (`ClaimCreate`, `ClaimResponse`).
- `backend/routers/claims.py`: endpoints de afirmaciones con autenticación JWT obligatoria:
  - `POST /claims` — envía una afirmación nueva
  - `GET /claims` — devuelve solo las afirmaciones del usuario autenticado
- Dependencia `get_current_user` que lee y valida el token Bearer en cada petición protegida.

### Problema encontrado (pendiente de resolver)
Al probar `POST /claims` en Swagger, error: `table "claims" does not exist`.


### Horas dedicadas
| Actividad | Tiempo |
|-----------|--------|
| Modelo ORM `Claim` y schemas Pydantic | 0h 45min |
| Router `/claims` con autenticación JWT | 1h |
| Pruebas en Swagger | 0h 15min |
| **Total sesión** | **2h** |

---

## Resumen acumulado

| Semana | Fecha | Horas |
|--------|-------|-------|
| Semana 1 | 15/02/2026 | 1h 30min |
| Semana 2 | 22/02/2026 | 1h 30min |
| Semana 3 | 26/02/2026 | 1h 15min |
| Semana 4 | 07/03/2026 | 6h 30min |
| Semana 5 | 26/03/2026 | 3h 30min |
| Semana 5 (s2) | 16/04/2026 | 3h |
| Semana 6 | 18/04/2026 | 2h |
| **TOTAL** | | **~19h 15min** |

---

> **Nota:** Este changelog se actualiza semanalmente y servirá como base
> para la planificación real del Plan de Trabajo final, donde se compararán
> las horas estimadas con las horas reales dedicadas a cada requisito del RFTP.

