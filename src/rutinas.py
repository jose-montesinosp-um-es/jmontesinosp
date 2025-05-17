from datetime import datetime
from bson import ObjectId

class Rutina:
    
    def __init__(self, nombre, usuario_id, musculos=[]):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.musculos = musculos
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
            {"$set": self.to_dict()},
            upsert=True
        )

    def eliminarMusculo(self, nombre_musculo):
        
        encontrado = False
        for m in self.musculos:
        
            if m.nombre == nombre_musculo:
                
                self.musculos.remove(m)
                encontrado = True
                break
            
        if not encontrado:
            raise ValueError(f"El músculo {nombre_musculo} no está en la lista de músculos.")
        self.guardar()
    
    def agregarMusculo(self, musculo_id, partes):
        self.musculos.append({
            'musculo_id': musculo_id,
            'partes': partes
        })
