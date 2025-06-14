from bson import ObjectId

class Musculo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ejercicios = []
        self._id = ObjectId()

    def formato(self):
        return {
            '_id': self._id,
            'nombre': self.nombre,
            'ejercicios': [e.formato() for e in self.ejercicios]
        }
    
    def guardar(self, db):
        db.musculos.update_one(
            {"_id": self._id},
            {"$set": self.formato()},
            upsert=True
        )

    def agregar_ejercicio(self, db, Ejercicio):
        self.ejercicios.append(Ejercicio)
        self.guardar(db)

    def eliminar_ejercicio(self, db, ejercicio):
        for e in self.ejercicios:
            if e['_id'] == ejercicio:
                self.ejercicios.remove(e)
        self.guardar(db)