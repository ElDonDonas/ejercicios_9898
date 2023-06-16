def busqueda_interpolacion(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin and lista[inicio] <= objetivo <= lista[fin]:
        estimacion = inicio + ((objetivo - lista[inicio]) * (fin - inicio)) // (lista[fin] - lista[inicio])

        if lista[estimacion] == objetivo:
            return estimacion
        elif lista[estimacion] < objetivo:
            inicio = estimacion + 1
        else:
            fin = estimacion - 1

    return -1

# Paso 1: Solicitar al usuario el número objetivo.
numero_objetivo = int(input("Ingrese el número objetivo: "))

# Paso 2: Crear una lista de números enteros ordenada de forma ascendente.
lista_numeros = [1, 3, 5, 7, 9, 11, 13, 15]

# Paso 3: Implementar la función de búsqueda por interpolación.
posicion = busqueda_interpolacion(lista_numeros, numero_objetivo)

# Paso 5: Imprimir la posición si se encuentra el número objetivo.
if posicion != -1:
    print("El número", numero_objetivo, "se encuentra en la posición", posicion)
else:
    print("El número", numero_objetivo, "no está presente en la lista.")
