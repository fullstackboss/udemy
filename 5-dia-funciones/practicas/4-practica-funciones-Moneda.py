from random import *
lista_numeros=[randint(1,3) for item in range(5)]
def lanzar_moneda():
    """suerte=randint(1,2)
    if suerte==1:
        suerte='Cara'
    else:
        suerte='Cruz'"""

    suerte = ['Cara', 'Cruz']
    return choice(suerte)

def probar_suerte(suerte,lista):
    if suerte=='Cara':
        print("La lista se autodestruirá")
        lista.clear()
    else:
        print("La lista fue salvada")
    return lista

misuerte=lanzar_moneda()
suerte=probar_suerte(misuerte,lista_numeros)
print(suerte)