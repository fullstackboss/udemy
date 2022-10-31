from random import *
#lista de palabras
listado=['kakaroto', 'vegeta','goku','trunks','gogeta',"bulma","yamcha","pikkoro"]


def selecciona(palabra):
    palabra = choice(listado)
    #print(f"la palabra seleccionada es: {palabra}")
    return palabra

def muestra_guiones(palabra):
    palabra_guiones = []
    for item in palabra:
        palabra_guiones.append('-')
    print(palabra_guiones)
    return palabra_guiones
def ingresar_letra():
    letra_usuario=input("Ingrese letra: ")
    while letra_usuario.isdigit()==True:
        letra_usuario.isalnum()
        print("Ingrese un caracter válido!")
        letra_usuario = input("Ingrese letra: ")
    else:
        pass
    return letra_usuario
def actualizar_guiones(listaguion, letra,palabra):
    for index, item in enumerate(palabra):
        if letra == item:
            listaguion[index] = letra
        else:
            pass
    return listaguion
def evalua(lista_guiones, letra, palabra, chance):
    if letra in palabra:
        lista=actualizar_guiones(lista_guiones, letra, palabra)
        print(lista)
    else:
        chance-=1
        print(f"Te queda {chance} oportunidades")
    return chance

def descontar(dato):
    dato-=1
    print(f"Te quedan {dato} oportunidades")
    return dato



oportunidades=5
print(f"\nBIENVENIDO AL JUEGO DEL AHORCADO....\nTENDRAS {oportunidades} OPORTUNIDADES: \n")

#Se elige la palabra desde lista
palabra_aleatoria=selecciona(listado)

#Genera y muestra la lista en guiones
lista_guiones=muestra_guiones(palabra_aleatoria)

while oportunidades > 1:
    #Solicita ingresar letra al usuario
    if '-' in lista_guiones:
        letra_usuario=ingresar_letra()
    else:
        print("MUY BIEN GANASTE!!!")
        break
    #Evalua la coincidencia
    oportunidades=evalua(lista_guiones, letra_usuario, palabra_aleatoria, oportunidades)
else:
    print("AHORCADO!!!!!")

