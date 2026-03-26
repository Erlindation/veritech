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

## Resumen acumulado

| Semana | Fecha | Horas |
|--------|-------|-------|
| Semana 1 | 15/02/2026 | 1h 30min |
| Semana 2 | 22/02/2026 | 1h 30min |
| Semana 3 | 26/02/2026 | 1h 15min |
| Semana 4 | 07/03/2026 | 6h 30min |
| **TOTAL** | | **~11h** |

---

> **Nota:** Este changelog se actualiza semanalmente y servirá como base
> para la planificación real del Plan de Trabajo final, donde se compararán
> las horas estimadas con las horas reales dedicadas a cada requisito del RFTP.

