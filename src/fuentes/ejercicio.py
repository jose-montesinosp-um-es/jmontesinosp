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

    def actualizarSeries(self, series):
        self.series = series
        self.guardar_en_db()
    
    def actualizarReps(self, serie, reps):
        self.reps[serie-1] = reps
        self.guardar_en_db()
    
    def actualizarCarga(self, serie, carga):
        self.carga[serie-1] = carga
        self.guardar_en_db()
    
    def actualizarRIR(self, rir):
        self.rir = rir
        self.guardar_en_db()