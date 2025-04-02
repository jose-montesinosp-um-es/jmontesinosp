from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.gimnasio  
rutinas_col = db.rutinas
musculos_col = db.musculos
ejercicios_col = db.ejercicios


class Rutina:
    
    def __init__(self, nombre, usuario, musculos):
        self.nombre = nombre
        self.usuario = usuario
        self.musculos = musculos

    def guardar_en_db(self):
        rutina_data = {
            "nombre": self.nombre,
            "musculos": self.musculos
        }
        db.rutinas.insert_one(rutina_data)
    
    def eliminarMusculo(self, musculo):
        if musculo not in self.musculos:
            raise ValueError(f"El músculo {musculo} no está en la lista de músculos.")
        
        for musculo in self.musculos:
            if musculo.nombre == musculo:
                break
        self.musculos.remove(musculo)   
        self.guardar_en_db()
    
    def agregarMusculo(self, musculo):
        self.musculos.append(musculo)
        self.guardar_en_db()

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.gimnasio

class Musculo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partes = []  # Lista de partes del músculo

    def guardar_en_db(self):
        musculo_data = {
            "musculo": self.nombre,
            "partes": self.partes
        }
        db.musculos.update_one(
            {"musculo": self.nombre},
            {"$set": musculo_data},
            upsert=True
        )

    def cargar_de_db(self):
        musculo_data = db.musculos.find_one({"musculo": self.nombre})
        if musculo_data:
            self.partes = musculo_data.get("partes", [])
        else:
            print(f"El músculo {self.nombre} no existe en la base de datos.")

    def agregar_parte(self, nombre_parte):
        # Comprueba si la parte ya existe
        for parte in self.partes:
            if parte["nombre"] == nombre_parte:
                print(f"La parte '{nombre_parte}' ya existe en el músculo '{self.nombre}'.")
                return
        
        # Si no existe, la añade con una lista vacía de ejercicios
        nueva_parte = {"nombre": nombre_parte, "ejercicios": []}
        self.partes.append(nueva_parte)
        self.guardar_en_db()
        print(f"Parte '{nombre_parte}' añadida al músculo '{self.nombre}'.")

    def agregar_ejercicio(self, nombre_parte, ejercicio):
        for parte in self.partes:
            if parte["nombre"] == nombre_parte:
                if ejercicio not in parte["ejercicios"]:
                    parte["ejercicios"].append(ejercicio)
                    self.guardar_en_db()
                    print(f"Ejercicio '{ejercicio}' añadido a la parte '{nombre_parte}' del músculo '{self.nombre}'.")
                else:
                    print(f"El ejercicio '{ejercicio}' ya existe en la parte '{nombre_parte}'.")
                return
        
        print(f"No se encontró la parte '{nombre_parte}' en el músculo '{self.nombre}'.")

    def eliminar_ejercicio(self, nombre_parte, ejercicio):
        for parte in self.partes:
            if parte["nombre"] == nombre_parte:
                if ejercicio in parte["ejercicios"]:
                    parte["ejercicios"].remove(ejercicio)
                    self.guardar_en_db()
                    print(f"Ejercicio '{ejercicio}' eliminado de la parte '{nombre_parte}'.")
                else:
                    print(f"El ejercicio '{ejercicio}' no está en la parte '{nombre_parte}'.")
                return
        
        print(f"No se encontró la parte '{nombre_parte}' en el músculo '{self.nombre}'.")

    def mostrar_musculo(self):
        print(f"\nMúsculo: {self.nombre}")
        for parte in self.partes:
            print(f"- Parte: {parte['nombre']}")
            print(f"  Ejercicios: {', '.join(parte['ejercicios']) if parte['ejercicios'] else 'Ninguno'}")

    
class Ejercicio:
    
    def __init__(self, nombre, series, reps, rir, equipo):
        self.nombre = nombre
        self.series = series
        self.reps = reps
        self.carga = None
        self.rir = rir
        self.equipo = equipo
    
    def guardar_en_db(self):
        ejercicio_data = {
            "ejercicio": self.nombre,
            "series": self.series,
            "reps": self.reps,
            "carga": self.carga,
            "rir": self.rir,
            "equipo": self.equipo
        }
        db.ejercicios.insert_one(ejercicio_data)
    
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
