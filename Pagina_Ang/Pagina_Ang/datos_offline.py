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


def sincronizar_datos_offline():
    """Guarda los registros offline en la base principal MySQL."""
    from django.contrib.auth.models import User
    from django.db import DatabaseError, OperationalError, connections
    from Pokemon.models import Pokemon

    if not ARCHIVO_DATOS_OFFLINE.exists():
        return 0

    try:
        alias = "mysql_primary" if "mysql_primary" in connections else "default"
        connections[alias].ensure_connection()
    except (DatabaseError, OperationalError):
        return 0

    try:
        with open(ARCHIVO_DATOS_OFFLINE, "r", encoding="utf-8") as archivo:
            registros = json.load(archivo)
    except (json.JSONDecodeError, OSError):
        return 0

    registros_pendientes = []
    cantidad_guardada = 0

    for registro in registros:
        operacion = registro.get("operacion")
        datos = registro.get("datos") or {}
        pokemon_id = registro.get("pokemon_id")

        try:
            if operacion in ("crear", "editar", "eliminar"):
                if operacion == "crear":
                    Pokemon.objects.using(alias).create(**datos)
                elif operacion == "editar":
                    pokemon = Pokemon.objects.using(alias).filter(pk=pokemon_id).first()
                    if pokemon:
                        for campo, valor in datos.items():
                            setattr(pokemon, campo, valor)
                        pokemon.save(using=alias)
                else:
                    Pokemon.objects.using(alias).filter(pk=pokemon_id).delete()

            elif operacion == "error_base_de_datos" and datos:
                if "username" in datos:
                    username = datos["username"]
                    if not User.objects.using(alias).filter(username=username).exists():
                        password = datos.get("password1") or datos.get("password")
                        user = User.objects.using(alias).create(
                            username=username, email=datos.get("email", "")
                        )
                        if password:
                            user.set_password(password)
                            user.save(using=alias)
                elif "Nombre" in datos:
                    Pokemon.objects.using(alias).create(
                        Nombre=datos.get("Nombre"),
                        Tipo=datos.get("Tipo") or None,
                        Descripcion=datos.get("Descripcion"),
                        Imagen=datos.get("Imagen") or None,
                    )
                else:
                    registros_pendientes.append(registro)
                    continue
            else:
                registros_pendientes.append(registro)
                continue

            cantidad_guardada += 1
        except (DatabaseError, OperationalError, TypeError, ValueError):
            registros_pendientes.append(registro)

    with open(ARCHIVO_DATOS_OFFLINE, "w", encoding="utf-8") as archivo:
        json.dump(registros_pendientes, archivo, ensure_ascii=False, indent=4)

    return cantidad_guardada
