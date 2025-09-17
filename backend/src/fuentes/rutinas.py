from datetime import datetime
from bson import ObjectId

class Rutina:
    
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.musculos = []
        self.fecha_creacion = datetime.utcnow()
        self._id = ObjectId()

    def formato(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "usuario_id": self.usuario_id,
            "fecha_creacion": self.fecha_creacion,
            "musculos": self.musculos
        }
    
    def guardar(self, db):
        db.rutinas.replace_one(
            {"_id": self._id},
            self.formato(),
            upsert=True
        )
    
    @classmethod
    def from_dict(cls, data):
        rutina = cls(
            nombre=data["nombre"],
            usuario_id=data["usuario_id"],
            _id=data["_id"]
        )
        rutina.musculos = data.get("musculos", [])
        rutina.fecha_creacion = data.get("fecha_creacion")
        return rutina

    def eliminarMusculo(self, db, nombre_musculo):
        
        for m in self.musculos:
            if m.nombre == nombre_musculo:
                self.musculos.remove(m)
                break

        self.guardar(db)
    
    def agregar_musculo(self, db_busqueda, db_insercion):
    # Mostrar todos los músculos disponibles
        musculos = list(db_busqueda.ejercicios.find({}))
    
        if not musculos:
            print("No hay músculos disponibles en la base de datos")
            return
    
        print("Músculos disponibles:")
        for i, musculo in enumerate(musculos, 1):
            print(f"{i}. {musculo['musculo']}")
    
        while True:
            eleccion = input("Elige un músculo (número o nombre): ").strip()
        
            musculo_seleccionado = None
        
            # Verificar si eligió por número
            if eleccion.isdigit():
                indice = int(eleccion) - 1
                if 0 <= indice < len(musculos):
                    musculo_seleccionado = musculos[indice]
            else:
                # Buscar por nombre
                for musculo in musculos:
                    if musculo['musculo'].lower() == eleccion.lower():
                        musculo_seleccionado = musculo
                        break
        
            if musculo_seleccionado:
                # Verificar si ya lo tiene
                if not hasattr(self, 'musculos'):
                    self.musculos = []
                
                if any(m['musculo'].lower() == musculo_seleccionado['musculo'].lower() for m in self.musculos):
                    print(f"Ya tienes el músculo '{musculo_seleccionado['musculo']}' en tu rutina.")
                else:
                    self.musculos.append({
                        "_id": musculo_seleccionado["_id"],
                        "nombre": musculo_seleccionado["nombre"]
                    })
                    self.guardar(db_insercion)
                    print(f"Músculo '{musculo_seleccionado['nombre']}' agregado correctamente.")
                break
            else:
                print("Músculo no encontrado. Intenta de nuevo.")

