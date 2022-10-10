"""Enumerate sirve para obetner datos de ua COLECCION"""

"""MODO clasico no recomendado en python"""
lista = ['a','b','c']
indice=0
for item in lista:
    print(indice, item)
    indice+=1

print("\n")

"""Mucho mejor y mas eficiente"""
for indice,item in enumerate(lista):
    print(indice, item)

print("\n")
for indice,item in enumerate(range(10,16)):
    print(indice,item)

mituple=list(enumerate(lista))
print(mituple)
print(mituple[1][0])
