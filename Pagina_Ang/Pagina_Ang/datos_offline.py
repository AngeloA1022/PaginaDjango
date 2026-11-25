import json
from datetime import datetime

from django.conf import settings


ARCHIVO_DATOS_OFFLINE = getattr(settings, "JSON_FALLBACK_FILE", settings.BASE_DIR / "datos_offline.json")

if not ARCHIVO_DATOS_OFFLINE.exists():
    with open(ARCHIVO_DATOS_OFFLINE, "w", encoding="utf-8") as archivo:
        json.dump([], archivo)


def guardar_datos_offline(operacion, datos=None, pokemon_id=None):
    registros = []

    if ARCHIVO_DATOS_OFFLINE.exists():
        try:
            with open(ARCHIVO_DATOS_OFFLINE, "r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
        except (json.JSONDecodeError, OSError):
            registros = []

    registros.append(
        {
            "fecha": datetime.now().isoformat(timespec="seconds"),
            "operacion": operacion,
            "pokemon_id": pokemon_id,
            "datos": datos or {},
        }
    )

    with open(ARCHIVO_DATOS_OFFLINE, "w", encoding="utf-8") as archivo:
        json.dump(registros, archivo, ensure_ascii=False, indent=4)
