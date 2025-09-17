from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from base_datos import get_db_catalogo
from bson import ObjectId
import time

# Configurar Selenium en modo headless
def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    return driver

# Scraping dinámico desde MuscleWiki
def scrape_musclewiki_dinamico(slug, musculo_nombre):
    driver = get_driver()
    db = get_db_catalogo()
    url = f"https://musclewiki.com/es-es/exercises/male/{slug}"
    driver.get(url)

    time.sleep(5)  # esperar carga del contenido dinámico

    enlaces = driver.find_elements(By.CSS_SELECTOR, "a[href^='/machine/male']")

    print(f"🔍 {musculo_nombre}: {len(enlaces)} ejercicios encontrados")

    for enlace in enlaces:
        try:
            href = enlace.get_attribute("href")
            if not href:
                continue
            nombre = href.strip("/").split("/")[-1].replace("-", " ").capitalize()

            data = {
                "_id": ObjectId(),
                "nombre": nombre,
                "musculo": musculo_nombre,
                "parte": "General",
                "fuente": "MuscleWiki",
                "video_url": href
            }

            db.ejercicios.update_one(
                {"nombre": data["nombre"], "musculo": data["musculo"]},
                {"$set": data},
                upsert=True
            )
        except Exception as err:
            print(f"⚠️ Error procesando ejercicio: {err}")

    driver.quit()

def almacenar_ejercicios(musculos):
    for slug, nombre in musculos.items():
        scrape_musclewiki_dinamico(slug, nombre)