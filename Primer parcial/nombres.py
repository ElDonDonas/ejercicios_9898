# Crear una lista de nombres
nombres = []

# Solicitar al usuario ingresar nombres hasta que ingrese "fin"
while True:
    nombre = input("Ingrese un nombre (o escriba 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nombres.append(nombre)

# Ordenar la lista de nombres alfabéticamente
nombres.sort()

# Mostrar los nombres en orden alfabético
print("Nombres en orden alfabético:")
for nombre in nombres:
    print(nombre)
