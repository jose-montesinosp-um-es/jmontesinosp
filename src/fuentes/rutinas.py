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
        db.rutinas.update_one(
            {"_id": self._id},
            {"$set": self.formato()},
            upsert=True
        )

    def eliminarMusculo(self, db, nombre_musculo):
        
        for m in self.musculos:
            if m.nombre == nombre_musculo:
                self.musculos.remove(m)
                break

        self.guardar(db)
    
    def agregar_musculo(self, db, Musculo):
        self.musculos.append(Musculo.formato())
        self.guardar(db)

