# VeriTech

> Aplicación web para verificación de información online basada en evidencias.

Autor: Erlinda Canillas Sánchez.

## ¿Qué es VeriTech?

VeriTech permite a usuarios registrados introducir afirmaciones factuales en lenguaje natural y recibir un veredicto estructurado (*Verificable*, *Engañoso* o *No comprobable*) respaldado por evidencias obtenidas de la Google Fact Check Tools API. Todas las consultas se almacenan en PostgreSQL para consulta posterior.

---

## Requisitos previos

| Herramienta | Versión mínima | Descarga |
|-------------|---------------|----------|
| Python | 3.11+ | https://www.python.org/downloads/ |
| PostgreSQL | 15+ | https://www.postgresql.org/download/windows/ |
| Git | cualquiera | https://git-scm.com/ |
| VS Code | cualquiera | https://code.visualstudio.com/ |

---

## Instalación paso a paso (Windows)

Este proyecto mantiene una estructura básica de backend y frontend donde comenzaré a desarrollar desde el backend arriba.

Primero, dentro del backend/, añado database.py, que me permitirá desplegar PostgreSQL — relacional, con tablas, filas y columnas que configuro en pgAdmin. Desde la URL en .env.template:

postgresql://usuario:contraseña@localhost:5432/veritech
Que ejecutará esta estructura:

- load_dotenv()	Lee .env y carga las variables
- DATABASE_URL	Coge la URL de conexión del .env
- create_engine(...)	Crea la conexión real a PostgreSQL
- SessionLocal	Fábrica de sesiones — cada petición HTTP obtiene la suya
- Base	Clase madre de todos mis modelos (tablas) — cuando se hace class User(Base), SQLAlchemy crea esa tabla
- get_db()	Función que FastAPI usará como dependencia en los endpoints — abre una sesión, la da al endpoint, y la cierra siempre aunque haya error