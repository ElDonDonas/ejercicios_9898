def busqueda_lineal(lista, objetivo):
    for i, numero in enumerate(lista):
        if numero == objetivo:
            return i
    return -1

# Paso 1: Solicitar al usuario el número objetivo.
numero_objetivo = int(input("Ingrese el número objetivo: "))

# Paso 2: Crear una lista de números enteros.
lista_numeros = [2, 5, 8, 10, 15, 20, 25]

# Paso 3: Implementar la función de búsqueda lineal.
posicion = busqueda_lineal(lista_numeros, numero_objetivo)

# Paso 4: Imprimir la posición si se encuentra el número objetivo.
if posicion != -1:
    print("El número", numero_objetivo, "se encuentra en la posición", posicion)
else:
    print("El número", numero_objetivo, "no está presente en la lista.")
