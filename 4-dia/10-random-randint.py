from random import randint
from random import *

aleatorio=randint(0,100)
print(aleatorio)

"""Valor decimal aleatorio"""
aleatorio2=round(uniform(1,10),1)
print(aleatorio2)

"""Valor decimal entre 0 y 1....es una fraccion de un entero"""
aleatorio3 = random()
print(aleatorio3)

"""Choice alaeatorio de una lista"""
colores= ['azul','rojo','verde','amarillo','anaranjado','blanco']
aleatorio4 = choice(colores)
print(aleatorio4)

"""Desordena los elementos de una lista"""
numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo=choice(nombres)
print(sorteo)
