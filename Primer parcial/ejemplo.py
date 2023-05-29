class Monster:

    def __init__(self, nombre, categoria):  # Corregido: "__init__" en lugar de "_init_"
        self.nombre = nombre
        self.categoria = categoria
    
    def __str__(self):  # Corregido: "__str__" en lugar de "_str_"
        return f"Soy {self.nombre} y mi categoría es {self.categoria}"

    def myFunc(self):
        print("Hey, soy un " + self.nombre)

monstruito = Monster("Sulivan", "Asustador")
print(monstruito.nombre)
print(monstruito)
monstruito.myFunc()
