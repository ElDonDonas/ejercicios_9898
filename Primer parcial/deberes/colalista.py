class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)


# Crear una instancia de la Cola
cola = Cola()

# Encolar números enteros
cola.encolar(10)
cola.encolar(20)
cola.encolar(30)

# Desencolar números enteros
print(cola.desencolar())  # Salida: 10
print(cola.desencolar())  # Salida: 20
print(cola.desencolar())  # Salida: 30
print(cola.desencolar())  # Salida: None (la cola está vacía)
