import time
import psutil

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def measure_resources():
    process = psutil.Process()
    cpu_percent = psutil.cpu_percent()
    memory_percent = process.memory_percent()
    return cpu_percent, memory_percent

# Prueba del algoritmo de ordenamiento ShellSort
data = [64, 34, 25, 12, 22, 11, 90]
print("Datos antes de ordenar:", data)

start_time = time.time()
start_cpu, start_memory = measure_resources()

shell_sort(data)

end_time = time.time()
end_cpu, end_memory = measure_resources()

print("Datos después de ordenar:", data)
print("Tiempo de ejecución:", end_time - start_time, "segundos")
print("Uso de CPU:", end_cpu - start_cpu, "%")
print("Uso de memoria:", end_memory - start_memory, "%")
