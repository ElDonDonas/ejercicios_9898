class Padre:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Hijo(Padre):
    def __init__(self, nombre, profesion) -> None:
        super().__init__(nombre)
        self.profesion = profesion

jorge = Hijo("Jorge", "Albanil")
Mariu = Hijo("Maria", "Modista")

