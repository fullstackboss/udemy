"""
por cada elemento en lista
    imprime("")

"""

lista=['kakaroto','vegeta','freezer',"Cooler", "KingCool","krilin"]

for elemento in lista:
    indice=lista.index(elemento)+1
    print(f"Te llamas {elemento} con posicion {indice}")


for nombre in lista:
    if nombre.startswith('k'):
        print(nombre)
    else:
        print('nombre que no commienza:' + nombre)

lista_numeros=[1,2,3,4,5]
mivalor=0

for elemento in lista_numeros:
    mivalor=mivalor+elemento

print("\n")
print(mivalor)

"""Los string son ITERABLES como una lista"""
palabra='insecto'
for letra in palabra:
    print(letra)

"""otra manera"""
for letra in 'insecto':
    print(letra)

"""Imprime simple"""
for variable in [[1,2],[3,4],[5,6]]:
    print(variable)

"""Imprime por elemento """
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)


print("\n")

"""Con diccionarios"""
dic={'clave1':'valor-a','clave2':'valor-b','clave3':'valor-c'}
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for a,b in dic.items():
    print(a,b)




