#CON RANGO
def detecta(numero):
    return numero in range(100,999)
"""
resultado=detecta(996)
print(resultado)
"""

#CON LISTA
def detectaenlista(lista):
    lista3=[]
    for item in lista:
        if item in range(100,1000):
            lista3.append(item)
        else:
            pass
    return lista3


resultado2=detectaenlista([55,655,109,55,955,505])
print(resultado2)

def todos_positivos(milista):
    for item in milista:
        if item <0:
            return False
        else:
            pass
    return True
res=todos_positivos([55,655,109,55,955,505])
print(res)


def suma_menores(infolista):
    total=0
    for item in infolista:
        if item >0 and item <1000:
           total=total+item
        else:
            pass
    return total
lista3=[0,2,4,100,-50,-10,20]
dato=suma_menores(lista3)
print(dato)


lista_numeros=[2,3,4,5,6,7,8]
def cantidad_pares(lista_numeros):
    pares=0
    for item in lista_numeros:
        if(item%2==0):
            pares+=1;
        else:
            pass
    return pares;
dato2=cantidad_pares(lista_numeros)
print(dato2)