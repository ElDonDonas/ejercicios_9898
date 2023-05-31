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


def es_simetrica(lista):
    pila = Pila()
    mitad = len(lista) // 2

    for i in range(mitad):
        pila.apilar(lista[i])

    if len(lista) % 2 == 1:
        inicio = mitad + 1
    else:
        inicio = mitad

    for i in range(inicio, len(lista)):
        elemento = pila.desapilar()
        if elemento != lista[i]:
            return False

    return True


# Ejemplo de uso
lista_1 = [1, 2, 3, 4, 3, 2, 1]
print(lista_1, "es simétrica:", es_simetrica(lista_1))  # Output: True

lista_2 = [1, 2, 3, 4, 5, 6]
print(lista_2, "es simétrica:", es_simetrica(lista_2))  # Output: False
