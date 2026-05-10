# Módulo que habla con la Google Fact Check Tools API.
# Recibe una afirmación en texto y devuelve un veredicto basado en lo que encuentre.
# Si no encuentra nada, devuelve "No comprobable" — no inventa resultados.
# Las credenciales y la URL base de la API se cargan desde el archivo .env.

import os
import httpx

GOOGLE_API_KEY = os.getenv("GOOGLE_FACT_CHECK_API_KEY")
GOOGLE_API_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search"


def check_claim(text: str) -> tuple[str, str | None]:
    if not GOOGLE_API_KEY:
        return "API no configurada", None

    try:
        response = httpx.get(
            GOOGLE_API_URL,
            params={"query": text, "key": GOOGLE_API_KEY},
            timeout=10.0,
        )
        response.raise_for_status()
        data = response.json()

        claims = data.get("claims", [])
        if not claims:
            return "No comprobable", None

        first_claim = claims[0]
        reviews = first_claim.get("claimReview", [])
        if not reviews:
            return "No comprobable", None

        review = reviews[0]
        verdict = review.get("textualRating", "Sin veredicto")
        source = review.get("url") or None
        return verdict, source

    except httpx.HTTPError:
        return "Error al consultar la API", None