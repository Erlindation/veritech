# Módulo que habla con la Google Fact Check Tools API.
# Recibe una afirmación en texto y devuelve un veredicto basado en lo que encuentre.
# Si no encuentra nada, devuelve "No comprobable" — no inventa resultados.
# Las credenciales y la URL base de la API se cargan desde el archivo .env.
# Este servicio es llamado desde el endpoint check_claim() y el resultado se guarda
# en la base de datos junto con la afirmación original.

import os
import httpx

GOOGLE_API_KEY = os.getenv("GOOGLE_FACT_CHECK_API_KEY")
GOOGLE_API_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search"


def check_claim(text: str) -> str:
    # Si no hay clave configurada, aviso claro en vez de un error críptico.
    if not GOOGLE_API_KEY:
        return "API no configurada"

    try:
        # Sin languageCode la API busca en todos los idiomas — más resultados.
        # Antes estaba hardcodeado a "es" y afirmaciones en inglés no devolvían nada.
        response = httpx.get(
            GOOGLE_API_URL,
            params={"query": text, "key": GOOGLE_API_KEY},
            timeout=10.0,
        )
        response.raise_for_status()
        data = response.json()

        # Si la API no devuelve claims, la afirmación no está en su base de datos.
        claims = data.get("claims", [])
        if not claims:
            return "No comprobable"

        # Cojo el primer resultado — el más relevante según Google.
        # Dentro puede haber varios fact-checkers; me quedo con el primero.
        first_claim = claims[0]
        reviews = first_claim.get("claimReview", [])
        if not reviews:
            return "No comprobable"

        verdict = reviews[0].get("textualRating", "Sin veredicto")
        return verdict

    except httpx.HTTPError:
        # Si la petición falla por red o por la API, no quiero que pete el endpoint.
        return "Error al consultar la API"
