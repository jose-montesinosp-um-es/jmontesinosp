from bson import ObjectId

class Ejercicio:
    def __init__(self, nombre, musculo, parte, equipo, series, popularidad=0):
        self.nombre = nombre
        self.musculo = musculo
        self.parte = parte
        self.equipo = equipo
        self.popularidad = popularidad
        self.series = series
        self.reps = []
        self.cargas = []
        self.rir = 0
        self._id = ObjectId()

    def formato(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "musculo": self.musculo,
            "parte": self.parte,
            "equipo": self.equipo,
            "popularidad": self.popularidad,
            "series": self.series,
            "reps": self.reps,
            "cargas": self.cargas,
            "rir": self.rir
        }

    def guardar(self, db):
        db.ejercicios.update_one(
            {"_id": self._id},
            {"$set": self.formato()},
            upsert=True
        )

    @classmethod
    def from_dict(cls, data):
        ejercicio = cls(
            nombre=data["nombre"],
            musculo=data["musculo"],
            descripcion=data.get("descripcion", ""),
            _id=data["_id"]
        )
        ejercicio.series = data.get("series", [])
        ejercicio.reps = data.get("reps", [])
        ejercicio.cargas = data.get("cargas", [])
        ejercicio.rir = data.get("rir", [])
        return ejercicio

    def actualizarSeries(self, series):
        self.series = series
        self.guardar()
    
    def actualizarReps(self, serie, reps):
        self.reps[serie-1] = reps
        self.guardar()
    
    def actualizarCarga(self, serie, carga):
        self.carga[serie-1] = carga
        self.guardar()
    
    def actualizarRIR(self, rir):
        self.rir = rir
        self.guardar()