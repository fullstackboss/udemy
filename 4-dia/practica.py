"""
Preguntar nombre
numero del 1 al 100...adivina en 8 intentos
por cada intento habra 4 opciones:
<1 o superior al Programa  a 100: no esta Permitido
< al Programa: respues incorrecta
> al Programa: respuesta incorrecta
= al Programa: Ha ganado y mostrar cuantos intentos le ha tomado
"""
from random import *
numero= randint(1,101)
#print(numero)
intento=8
print("He pensado en un numero y debe adivinarlo")
print("Tienes 8 intentos")
while intento>0:

    print(f"Estas en el Intento Nº {intento}")

    numero_user = int(input("ingresa tu numero:"))
    if (numero_user<1) or (numero_user>100):
        print("Numero No permitido")
        print("-------------------------")
    else:
        intento -= 1
        if numero_user==numero:
            print("!!!!GANASTE!!!!")
            break
        elif (numero_user<numero):
            print("El numero debe ser MAYOR")
            print("-------------------------")
            continue
        elif (numero_user>numero):
            print("El numero debe ser MENOR")
            print("-------------------------")
            continue
else: print("Perdiste")