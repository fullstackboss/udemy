milista=["rojo","verde","azul"]
resultado=len(milista)
print(resultado)

"""-----muestra elementos----"""
resultado_len=milista[0]
resultado_len=milista[0:3]
resultado_len=milista[0:]
print(resultado_len)


"""-----Suma listas----"""
milista2=["naranja","violeta","morado"]
print(milista+milista2)


"""-----crea una nueva lista----"""
milista3=milista+milista2
print(milista3)

"""-----cambia un elemento de la lista----"""
milista3[0]="CYAN"
print(milista3)

"""-----APPEND agrega un elemento de la lista----"""
milista3.append("CELESTE")
print(milista3)

"""-----POP eliminar un elemento de la lista----"""
"""por defecto elimina el ultimo elemento"""
"""milista3.pop()"""
milista3.pop(4)
print(milista3)

"""-----SORT y REVERSE ordena una lista: sort es un metodo que solo ordena...no devuelve nada----"""
lista_ordenada = ['a','o','g','m','p','z']
lista_desordenada = ['a','o','g','m','p','z']
lista_ordenada.sort()
lista_desordenada.reverse()
print(lista_ordenada)
print(lista_desordenada)






