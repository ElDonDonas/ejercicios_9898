dato = input("ingrese un dato: ")

print(dato)

lista = ["hola", "mundo"]

if lista.count(dato)>0:
    print("esta informacion existe: ", dato)
else:
    print("esta informacion no existe: ", dato)


primernumero = input("ingrese el primer numero")
segundonumero = input("ingrese el segundo numero")

primernumero = int(primernumero)
segundonumero = int(segundonumero)
print(type(primernumero))

print(primernumero + segundonumero)

