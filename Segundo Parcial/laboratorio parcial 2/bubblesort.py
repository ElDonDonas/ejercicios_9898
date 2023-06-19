import time
import psutil

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def measure_resources():
    process = psutil.Process()
    cpu_percent = psutil.cpu_percent()
    memory_percent = process.memory_percent()
    return cpu_percent, memory_percent

# Prueba del algoritmo de ordenamiento Burbuja
data = [64, 34, 25, 12, 22, 11, 90]
print("Datos antes de ordenar:", data)

start_time = time.time()
start_cpu, start_memory = measure_resources()

bubble_sort(data)

end_time = time.time()
end_cpu, end_memory = measure_resources()

print("Datos después de ordenar:", data)
print("Tiempo de ejecución:", end_time - start_time, "segundos")
print("Uso de CPU:", end_cpu - start_cpu, "%")
print("Uso de memoria:", end_memory - start_memory, "%")
