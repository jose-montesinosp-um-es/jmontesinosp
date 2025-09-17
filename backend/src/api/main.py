import sys
import os
# Agregar la ruta raíz del proyecto al PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, project_root)

from fastapi import FastAPI
from backend.src.fuentes import usuario, ejercicio, musculo, progreso, rutinas
from backend.src.api.base_datos import get_db_usuarios, get_db_catalogo

app = FastAPI(docs_url=None, redoc_url=None)

if __name__=='__main__':
    Pepe =  usuario.Usuario('Pepe', 'pepe@gmail.com')
    bd_usuarios = get_db_usuarios()
    bd_catalogo = get_db_catalogo()
    
    Pepe.guardar(bd_usuarios)
    rut1 = rutinas.Rutina('Press', Pepe._id)
    Pepe.agregar_rutina(bd_usuarios, rut1)
    print(Pepe.formato())
    rut1.agregar_musculo(bd_catalogo, bd_usuarios)

