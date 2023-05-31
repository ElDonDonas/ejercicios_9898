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


# Crear una instancia de la Pila
pila = Pila()

# Apilar elementos
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)

# Desapilar elementos
print(pila.desapilar())  # Salida: 30
print(pila.desapilar())  # Salida: 20
print(pila.desapilar())  # Salida: 10
print(pila.desapilar())  # Salida: None (la pila está vacía)
