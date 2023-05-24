#tuplas

tupla = ()
"""print(type(tupla))
tupla.append("Diego")"""
print(tupla)
tupla2 = ("juanito", "Pedrito", "Tuamam", "Pedrito")
print(tupla2)
print(tupla2.count("juanito"))
print(tupla2.count("Pedrito"))
print(tupla2.index("Pedrito"))

print(tupla2[2])

lista = list(tupla2)

print(type(lista))

lista.append("Mario")
print(lista)

tupla2 = tuple(lista)
print(tupla2)

#Range
rango = range(6)
print(rango)

#set

set = {2, 3, 4, 5, 6, 6}
print(set)
print(type(set))

#diccionario

cliente001 = {
    "Nombre" : "Diego",
    "Cedula" : 123812731,
    "Celular" : "09210391263",
    "Correo" : "oqgwehajksd@gmail.com"        
}

print(cliente001)
print(type(cliente001))
print(cliente001["Correo"])
print(cliente001.get("Celular"))
cliente001["Nombre"] = "Juan"
print(cliente001.get("Nombre"))

cliente001.popitem()
print(cliente001)
cliente001.pop("Celular")
print(cliente001)

del cliente001["Cedula"]
print(cliente001)

cliente002 = dict(cliente001)
print(cliente001)
print(cliente001)

#boolean

nacidovivo = True
agentecredito = False

print(type(nacidovivo))
print(type(agentecredito))

print(2>5)

if 2>8 :
    print("2 es mayor que 8")
elif 10>20:
    print("10 es menor a 20")
elif 100<=80:
    print("100 es mayor o igual que 80")
elif 80 >= 100:
    print("80 es menor que 100")
else:
    print("no se cumplio ninguna condicion anterior xd")

#operadores ternarios

if 2<10: print("2 es menor que 10")

print("se imprime si la condicion es verdadera") if 10 > 2 else print("se imprime si la condicion es falsa")

# And Or y Not ////////////////////////////////////////////////////////////////////////////////////

if 2<9 and 10<20:
    print("2 es mayor que 9 y 10 es menor que 20")

if 100<1000 or 20>900:
    print("100 es mejor que 1000 o 20 es mayor que 900")

