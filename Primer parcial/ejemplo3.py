class Gato:

    def __init__(self, nombre, edad, peso, altura, raza):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.raza = raza


    def __str__(self) -> str:
        return f"{self.nombre} es un gato que tiene {self.edad} anios"
    def dormir(self):
        return f"Yo soy {self.nombre} y duermo 13 horas al dia, mido {self.altura}cm"
    
    def comer(self):
        return f"yo soy {self.nombre} y como mucho, peso {self.peso}kg"
    
gato1 = Gato("Rocky", 3, 15, 60, "Persa")
print (gato1)
print (gato1.edad)
print (gato1.dormir())
print(gato1.comer())
