from random import *
#lista de palabras
listado=['kakaroto', 'vegeta','gokuko','trunkus','gogeta',"bulmab","ulonu"]
chances=3

def generar(palabra):
    palabra = choice(listado)
    print(f"la palabra seleccionada es: {palabra}")
    return palabra

def muestra_guiones(palabra):
    palabra_guiones = []
    for item in palabra:
        palabra_guiones.append('-')
    print(palabra_guiones)
    return palabra_guiones


def ingresar_letra():
    letra_usuario=input("Ingrese letra: ")
    #validando
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
    print(listaguion)
    return listaguion

def descontar(dato):
    dato-=1
    print(f"Te quedan {dato} oportunidades")
    return dato

def evalua_coincidencia(mugu,letra,palabra, chance):
    if letra in palabra:
        print(f"la letra {letra} SI esta en la palabra {palabra}")
        actualizar_guiones(mugu,letra,palabra)
    else:
        print(f"la letra {letra} NO esta en la palabra {palabra}")
        descontar(chance)



#Se elige la palabra desde lista
palabra_aleatoria=generar(listado)

#Genera y muestra la lista en guiones
lista_guiones=muestra_guiones(palabra_aleatoria)

#Solicita ingresar letra al usuario
letra_usuario=ingresar_letra()

#Evalua la coincidencia
evalua_coincidencia(lista_guiones,letra_usuario,palabra_aleatoria, chances)

