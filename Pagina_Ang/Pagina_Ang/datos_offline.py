import json
from datetime import datetime

from django.conf import settings


ARCHIVO_DATOS_OFFLINE = settings.BASE_DIR / "datos_offline.json"


def guardar_datos_offline(operacion, datos=None, pokemon_id=None):
    registro = {
        "fecha": datetime.now().isoformat(timespec="seconds"),
        "operacion": operacion,
        "pokemon_id": pokemon_id,
        "datos": datos or {},
    }

    if ARCHIVO_DATOS_OFFLINE.exists():
        with open(ARCHIVO_DATOS_OFFLINE, "r", encoding="utf-8") as archivo:
            try:
                registros = json.load(archivo)
            except json.JSONDecodeError:
                registros = []
    else:
        registros = []

    registros.append(registro)

    with open(ARCHIVO_DATOS_OFFLINE, "w", encoding="utf-8") as archivo:
        json.dump(registros, archivo, ensure_ascii=False, indent=4)
