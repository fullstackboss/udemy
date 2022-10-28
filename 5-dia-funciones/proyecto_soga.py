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
    if '-' in listaguion:

        #print("Hay guiones aun")
        for index, item in enumerate(palabra):
                if letra == item:
                    listaguion[index] = letra
                else:
                    pass
    else:
        print("GANASTE!!!!!")

    return listaguion
def evalua_coincidencia(mugu,letra,palabra, chance):
    if letra in palabra:
        #print(f"la letra {letra} SI esta en la palabra {palabra}")
        lista=actualizar_guiones(mugu,letra,palabra)
        print("actualizando: ", lista)
        if '-' in mugu:
            print("continua")
            estado=False
        else:
            estado=True
            print("GANASTE!!!!")
            return estado
    else:
        #print(f"la letra {letra} NO esta en la palabra {palabra}")
        chance-=1
        print(f"Te queda {chances} oportunidades")
        return chance
def descontar(dato):
    dato-=1
    print(f"Te quedan {dato} oportunidades")
    return dato


print(f"BIENVENIDO AL JUEGO DEL AHORCADO, \nTendras {chances} oportunidades: ")

#Se elige la palabra desde lista
palabra_aleatoria=generar(listado)

#Genera y muestra la lista en guiones
print("INTENTA ADIVINAR LA PALABRA:")
lista_guiones=muestra_guiones(palabra_aleatoria)


while chances != 0:
    #Solicita ingresar letra al usuario
    letra_usuario=ingresar_letra()
    #Evalua la coincidencia
    #evalua_coincidencia(lista_guiones,letra_usuario,palabra_aleatoria, chances)
    chances=evalua_coincidencia(lista_guiones,letra_usuario,palabra_aleatoria, chances)

else:
    print("AHORCADO!!!!!")

