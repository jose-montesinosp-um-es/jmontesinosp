from fastapi import FastAPI
from musclewiki_scraper import almacenar_ejercicios

app = FastAPI(docs_url=None, redoc_url=None)

musculos = {
    "traps": "Trapecios",
    "quads": "Cuádriceps",
    "hamstrings": "Isquiotibiales",
    "calves": "Gemelos",
    "biceps": "Bíceps",
    "triceps": "Tríceps",
    "shoulders": "Hombros",
    "chest": "Pecho",
    "abdominals": "Abdominales",
    "glutes": "Glúteos",
    "forearms": "Antebrazo",
    "lowerback": "Espalda baja",
    "lats": "Dorsales",
    "traps-middle": "Espalda alta"
}

if __name__=='__main__':
    print('inicio')
    almacenar_ejercicios(musculos)
    print('fin')