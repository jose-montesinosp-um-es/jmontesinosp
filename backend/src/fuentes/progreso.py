from datetime import datetime
from bson import ObjectId

class Progreso:
    def __init__(self, usuario_id, rutina_id, ejercicio_id, series, rir, fecha=None):
        self.usuario_id = usuario_id
        self.rutina_id = rutina_id
        self.ejercicio_id = ejercicio_id
        self.series = series
        self.rir = rir
        self.fecha = fecha or datetime.utcnow()
        self._id = ObjectId()

    def formato(self):
        return {
            "_id": self._id,
            "usuario_id": self.usuario_id,
            "rutina_id": self.rutina_id,
            "ejercicio_id": self.ejercicio_id,
            "series": self.series,
            "rir": self.rir,
            "fecha": self.fecha
        }

    def guardar(self, db):
        db.progreso.replace_one(
            {"_id": self._id},
            self.formato(),
            upsert=True
        )

    @classmethod
    def from_dict(cls, data):
        progreso = cls(
            usuario_id=data["usuario_id"],
            rutina_id=data["rutina_id"],
            ejercicio_id=data["ejercicio_id"],
            series=data.get("series", []),
            reps=data.get("reps", []),
            cargas=data.get("cargas", []),
            rir=data.get("rir", []),
            fecha=data.get("fecha"),
            _id=data["_id"]
        )
        return progreso