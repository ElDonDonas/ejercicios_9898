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

    def obtener_tamano(self):
        return len(self.items)


# Ejemplo de uso
cola = Cola()
print("¿La cola está vacía?", cola.esta_vacia())  # Output: True

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("¿La cola está vacía?", cola.esta_vacia())  # Output: False
print("Tamaño de la cola:", cola.obtener_tamano())  # Output: 3

elemento = cola.desencolar()
print("Elemento desencolado:", elemento)  # Output: 1
print("Tamaño de la cola:", cola.obtener_tamano())  # Output: 2
