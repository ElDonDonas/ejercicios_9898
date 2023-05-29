class Madre:
    def __init__(self, apellidom) -> None:
        self.apellidom = apellidom

class Padre:
    def __init__(self, apellidop) -> None:
        self.apellidop = apellidop

class Hijo(Madre, Padre):
    def __init__(self, apellidom, apellidop, nombre, profesion) -> None:
        super().__init__(apellidom)  # Se llama al constructor de la clase Madre
        Padre.__init__(self, apellidop)  # Se llama al constructor de la clase Padre
        self.nombre = nombre
        self.profesion = profesion

Pedro = Hijo("Rodriguez", "Gonzalez", "Juan", "Arquitecto")
print(Pedro.nombre, Pedro.apellidop, Pedro.apellidom, Pedro.profesion)
