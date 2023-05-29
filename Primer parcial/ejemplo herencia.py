class Profesion:
    def __init__(self, nombre_profesion):
        self.nombre_profesion = nombre_profesion
    
    def mostrar_profesion(self):
        print(f"Profesión: {self.nombre_profesion}")

class Habilidades:
    def __init__(self, habilidades):
        self.habilidades = habilidades
    
    def mostrar_habilidades(self):
        print(f"Habilidades: {', '.join(self.habilidades)}")

class AniosEjercicio:
    def __init__(self, anios_ejercicio):
        self.anios_ejercicio = anios_ejercicio
    
    def mostrar_anios_ejercicio(self):
        print(f"Años de ejercicio: {self.anios_ejercicio}")

class Persona(Profesion, Habilidades, AniosEjercicio):
    def __init__(self, nombre, nombre_profesion, habilidades, anios_ejercicio):
        self.nombre = nombre
        Profesion.__init__(self, nombre_profesion)
        Habilidades.__init__(self, habilidades)
        AniosEjercicio.__init__(self, anios_ejercicio)
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        self.mostrar_profesion()
        self.mostrar_habilidades()
        self.mostrar_anios_ejercicio()

# Crear una persona y mostrar su información
persona = Persona("Juan", "Ingeniero", ["Programación", "Diseño"], 5)
persona.mostrar_informacion()
