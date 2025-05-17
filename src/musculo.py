from bson import ObjectId

class Musculo:
    def __init__(self, nombre, partes=[]):
        self.nombre = nombre
        self.partes = partes
        self._id = ObjectId()

    def formato(self):
        return {
            '_id': self._id,
            'nombre': self.nombre,
            'partes': self.partes
        }
    
    def guardar(self, db):
        db.musculos.update_one(
            {"_id": self._id},
            {"$set": self.to_dict()},
            upsert=True
        )

    def cargar_de_db(self, db):
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
