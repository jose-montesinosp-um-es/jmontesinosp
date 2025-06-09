import requests
from base_datos import get_db_catalogo
from bson import ObjectId
import re

def limpiar_html(texto):
    return re.sub(r"<[^>]*>", ", ", texto).strip()

def generar_base():
    db = get_db_catalogo()
    url = 'https://wger.de/api/v2/exerciseinfo/?limit=1000'

    datos = requests.get(url)
    if datos.status_code == 200:
        datos = datos.json()
        for ejercicio in datos['results']:

            traducciones_en = [
                t for t in ejercicio.get("translations", [])
                if t.get("language") == 2 and t.get("name") and t.get("description")
            ]
            if not traducciones_en:
                continue

            traduccion = traducciones_en[0]
            ej = traduccion["name"].strip()
            descripcion = limpiar_html(traduccion["description"])
            musculo = ejercicio["category"]["name"].strip()

            data = {
                "_id": ObjectId(),
                "nombre": ej,
                "musculo": musculo,
                "descripcion": descripcion,
            }

            filtro = {"nombre": data["nombre"], "musculo": data["musculo"]}

            datos_actualizables = data.copy()
            datos_actualizables.pop("_id")

            db.ejercicios.update_one(
                filtro,
                {
                    "$setOnInsert": {"_id": data["_id"]},
                    "$set": datos_actualizables
                },
                upsert=True
            )
            print(f"✅ Insertado: {ej} ({musculo})")
