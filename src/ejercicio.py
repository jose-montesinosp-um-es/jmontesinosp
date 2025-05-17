from bson import ObjectId

class Ejercicio:
    def __init__(self, nombre, musculo, parte, equipo, popularidad=0, _id=None):
        self.nombre = nombre
        self.musculo = musculo
        self.parte = parte
        self.equipo = equipo
        self.popularidad = popularidad
        self._id = _id or ObjectId()

    def formato(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "musculo": self.musculo,
            "parte": self.parte,
            "equipo": self.equipo,
            "popularidad": self.popularidad
        }

    def guardar(self, db):
        db.ejercicios.update_one(
            {"_id": self._id},
            {"$set": self.formato()},
            upsert=True
        )

    
    def actualizarSeries(self, series):
        self.series = series
        self.guardar_en_db()
    
    def actualizarReps(self, reps):
        self.reps = reps
        self.guardar_en_db()
    
    def actualizarCarga(self, carga):
        self.carga = carga
        self.guardar_en_db()
    
    def actualizarRIR(self, rir):
        self.rir = rir
        self.guardar_en_db()