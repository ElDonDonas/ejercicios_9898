def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Ejemplo de uso:
array = [11, 22, 25, 34, 64, 90]
target = 34
result = binary_search(array, target)

if result != -1:
    print("Elemento encontrado en la posición:", result)
else:
    print("Elemento no encontrado en el arreglo.")
