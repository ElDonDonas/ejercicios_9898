class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def obtener_tamano(self):
        return len(self.items)


# Ejemplo de uso
pila = Pila()
print("¿La pila está vacía?", pila.esta_vacia())  # Output: True

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print("¿La pila está vacía?", pila.esta_vacia())  # Output: False
print("Tamaño de la pila:", pila.obtener_tamano())  # Output: 3

elemento = pila.desapilar()
print("Elemento desapilado:", elemento)  # Output: 3
print("Tamaño de la pila:", pila.obtener_tamano())  # Output: 2
