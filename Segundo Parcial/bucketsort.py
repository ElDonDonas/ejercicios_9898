def distribution_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val

    for num in arr:
        count[num - min_val] += 1

    output = []
    for i in range(range_val):
        output.extend([i + min_val] * count[i])

    return output

# Ejemplo de uso
array = [9, 5, 2, 8, 1, 6, 3]
sorted_array = distribution_sort(array)
print("Array ordenado:")
print(sorted_array)