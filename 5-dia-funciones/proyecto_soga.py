from random import *
#lista de palabras
listado=['kakaroto', 'vegeta','goku','trunks','gogeta']

#selecion alaeatoria
def selecciona_palabra(lista):
    palabra_adivinar=choice(lista)
    # descompone en caracteres
    print("la palabra es:", palabra_adivinar)
    palabra_separada=list(palabra_adivinar)

    # Pinta guiones
    lista_mostrada=[]
    for item in palabra_separada:
        lista_mostrada.append('-')

    print(palabra_separada)
    print(lista_mostrada)

    chances=4
    print(f"tienes {chances} oportunidades")

    # Pide al usuario
    letra_user = input("ingrese letra: ")

    # Busca letra
    if letra_user in palabra_separada:
        print("Si esta")
        for index,item in enumerate(palabra_separada):
            if letra_user==item:
                lista_mostrada[index]=letra_user
            else:
                pass
    else:
        print("no esta")
        chances-=1
    print("LISTA FINAL:", lista_mostrada)
    print(f"Tienes {chances} oportunidades:")
    print(lista_mostrada)



#evalua si gano
resultado=selecciona_palabra(listado)
