lista_numeros=[1,2,15,7,2,7,25,91,25,6,1,23]
def reducir_lista(lista):
    mituple=set(lista)
    neolista=list(mituple)
    mayor=0
    ubicacion=0
    for index,item in enumerate(neolista):
        if item > mayor:
            ubicacion=index
            mayor=item
        else:
            pass
    #print(f"la ubicacion seria:{ubicacion} con el valor:{mayor}")
    neolista.pop(ubicacion)
    return neolista

def promedio(lista):
    suma=0
    for item in lista:
        suma += int(item)
    promedio=suma/len(lista)
    return promedio

datos=reducir_lista(lista_numeros)
print(datos)
pro=promedio(datos)
print(pro)

