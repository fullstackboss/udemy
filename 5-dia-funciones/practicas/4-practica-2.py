def recibe(palabra):
    lista_separada=list(set(list(palabra)))
    lista_separada.sort()
    return lista_separada

resultado=recibe("kakaroto")
print(resultado)


def numeros(*var):
    posicion=0
    for index,valor in enumerate(var):
        if valor==0:
            posicion=index

            if posicion + 1 == len(var):
                return False

            elif var[posicion+1]==0:
                return True

    return False

def numeros2(*var):
    contador=0
    for item in var:
        if contador + 1 == len(var):
            return False
        elif var[contador]==0 and var[contador+1]==0:
            return True
        else:
            contador+=1
    return False


print(numeros(0,90,35,70,70,13,0,0))
print(numeros2(0,70,35,9,60,13,0,0))
