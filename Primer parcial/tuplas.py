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
