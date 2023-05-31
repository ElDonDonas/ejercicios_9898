def verificar_orden_ascendente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Ejemplo de uso
mi_lista = [1, 2, 4, 3, 5]
if verificar_orden_ascendente(mi_lista):
    print("La lista está ordenada de forma ascendente.")
else:
    print("La lista no está ordenada de forma ascendente.")
