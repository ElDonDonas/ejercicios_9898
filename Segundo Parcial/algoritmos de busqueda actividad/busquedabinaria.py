def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

# Paso 1: Solicitar al usuario el número objetivo.
numero_objetivo = int(input("Ingrese el número objetivo: "))

# Paso 2: Crear una lista de números enteros ordenada de forma ascendente.
lista_numeros = [1, 3, 5, 7, 9, 11, 13, 15]

# Paso 3: Implementar la función de búsqueda binaria.
posicion = busqueda_binaria(lista_numeros, numero_objetivo)

# Paso 4: Imprimir la posición si se encuentra el número objetivo.
if posicion != -1:
    print("El número", numero_objetivo, "se encuentra en la posición", posicion)
else:
    print("El número", numero_objetivo, "no está presente en la lista.")
