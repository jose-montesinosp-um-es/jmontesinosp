from bson import ObjectId

class Usuario:
    def __init__(self, nombre, email, _id=None):
        self._id = _id or ObjectId()
        self.nombre = nombre
        self.email = email
        self.rutinas = []
        self.amigos = []
        self.solicitudesRecibidas = []
        self.solicitudesEnviadas = []

    def formato(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "email": self.email,
            "rutinas": self.rutinas,
            "amigos": self.amigos,
            "solicitudesRecibidas": self.solicitudesRecibidas, 
            "solicitudesEnviadas": self.solicitudesEnviadas
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

    @classmethod
    def from_dict(cls, data):
        usuario = cls(
            nombre=data["nombre"],
            email=data["email"],
            _id=data["_id"]
        )
        usuario.rutinas = data.get("rutinas", [])
        usuario.amigos = data.get("amigos", [])
        usuario.solicitudesRecibidas = data.get("solicitudesRecibidas", [])
        usuario.solicitudesEnviadas = data.get("solicitudesEnviadas", [])
        return usuario

    @classmethod
    def cargar_por_id(cls, db, usuario_id):
        data = db.usuarios.find_one({"_id": usuario_id})
        if data:
            return cls.from_dict(data)  # debes definir `from_dict`
        return None

    def agregar_amigo(self, db, amigo_id):
        if amigo_id not in self.amigos:
            self.amigos.append(amigo_id)
        self.guardar(db)

    def enviar_solicitud(self, db, amigo_id):
        if amigo_id not in self.solicitudesEnviadas:
            self.solicitudesEnviadas.append(amigo_id)
            amigo = Usuario.cargar_por_id(db, amigo_id)
            amigo.recibir_solicitud(db, self._id)
        self.guardar(db)

    def recibir_solicitud(self, db, amigo_id):
        if amigo_id not in self.solicitudesRecibidas:
            self.solicitudesRecibidas.append(amigo_id)
        self.guardar(db)

    def aceptar_solicitud(self, db, amigo_id):
        if amigo_id in self.solicitudesRecibidas:
            self.solicitudesRecibidas.remove(amigo_id)
            self.amigos.append(amigo_id)
            amigo = Usuario.cargar_por_id(db, amigo_id)
            amigo.agregar_amigo(db, self._id)
            amigo.solicitudesEnviadas.remove(self._id)
        self.guardar(db)