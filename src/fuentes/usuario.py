from bson import ObjectId

class Usuario:
    def __init__(self, nombre, email, _id=None):
        self._id = _id or ObjectId()
        self.nombre = nombre
        self.email = email
        self.rutinas = []

    def formato(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "email": self.email,
            "rutinas": self.rutinas
        }

    def guardar(self, db):
        db.usuarios.update_one(
            {"_id": self._id},
            {"$set": self.formato()},
            upsert=True
        )

    def agregar_rutina(self, db, Rutina):
        self.rutinas.append(Rutina.formato())
        self.guardar(db)
