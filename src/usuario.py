from bson import ObjectId

class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self._id = ObjectId()

    def formato(self):
        return {
            '_id': self._id,
            'nombre': self.nombre,
            'email': self.email
        }

    def guardar(self, db):
        db.usuarios.update_one(
            {"_id": self._id},
            {"$set": self.to_dict()},
            upsert=True
        )