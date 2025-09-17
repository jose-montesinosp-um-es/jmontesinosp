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
        db.musculos.replace_one(
            {"_id": self._id},
            self.formato(),
            upsert=True
        )
    
    @classmethod
    def from_dict(cls, data):
        musculo = cls(
            nombre=data["nombre"],
            _id=data["_id"]
        )
        musculo.ejercicios = data.get("ejercicios", [])
        return musculo

    def agregar_ejercicio(self, db, Ejercicio):
        self.ejercicios.append(Ejercicio)
        self.guardar(db)

    def eliminar_ejercicio(self, db, ejercicio):
        for e in self.ejercicios:
            if e['_id'] == ejercicio:
                self.ejercicios.remove(e)
        self.guardar(db)