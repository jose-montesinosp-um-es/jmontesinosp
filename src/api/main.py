from fastapi import FastAPI
from wger_api import generar_base

app = FastAPI(docs_url=None, redoc_url=None)

if __name__=='__main__':
    print('inicio')
    generar_base()
    print('fin')