def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

# Solicitar al usuario una lista de números
numbers = input("Ingresa una lista de números separados por espacios: ").split()
numbers = [int(num) for num in numbers]

# Ordenar la lista utilizando el algoritmo Quicksort
sorted_numbers = quicksort(numbers)

# Imprimir la lista ordenada
print("Lista ordenada:")
print(sorted_numbers)