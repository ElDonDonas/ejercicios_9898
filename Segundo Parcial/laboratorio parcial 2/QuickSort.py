import time
import psutil

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def measure_resources():
    process = psutil.Process()
    cpu_percent = psutil.cpu_percent()
    memory_percent = process.memory_percent()
    return cpu_percent, memory_percent

# Prueba del algoritmo de ordenamiento Quicksort
data = [64, 34, 25, 12, 22, 11, 90]
print("Datos antes de ordenar:", data)

start_time = time.time()
start_cpu, start_memory = measure_resources()

data = quicksort(data)

end_time = time.time()
end_cpu, end_memory = measure_resources()

print("Datos después de ordenar:", data)
print("Tiempo de ejecución:", end_time - start_time, "segundos")
print("Uso de CPU:", end_cpu - start_cpu, "%")
print("Uso de memoria:", end_memory - start_memory, "%")
