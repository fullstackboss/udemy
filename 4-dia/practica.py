"""productos=12
while productos>=0:
    print(f"tienes {productos} en lista")
    productos -=1
print("Se acabaron")
"""

numero = 50
while numero>=0:
    if numero%5==0:
        print(numero)
    numero -=1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for elemento in lista_numeros:
    if elemento>0:
        print(elemento)
    else:
        break

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


palabra="Python"
lista_indices=list(enumerate(palabra))
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,valor in enumerate(lista_nombres):
    if valor[0]=='M':
        print(indice,valor)
