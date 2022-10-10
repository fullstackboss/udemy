for elemento in range(1,11,2):
    print(elemento)

lista =list(range(1,31))
print(lista)


mi_lista = list(range(3,301,3))
print(mi_lista)

milista = list(range(1,16))
suma_cuadrados=0
cuadrado=0
for elemento in milista:
    cuadrado=elemento**2
    suma_cuadrados=suma_cuadrados+cuadrado
    print(f"el cuadrado de {elemento} es {cuadrado}")
print(f"El total de todo es: {suma_cuadrados}")
