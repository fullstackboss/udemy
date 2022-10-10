palabra='python'
lista=[]
for letra in palabra:
    lista.append(letra)
print(lista)

"""Optimizado"""
palabra='python'
lista=[letra for letra in 'python']
print(lista)

lista2 = [n for n in range(0,20,2)]
print(lista2)

lista2 = [n if n*2>10 else 'no' for n in range(0,20,2)]
print(lista2)

pies=[10,20,30,40,50]
metros=[round(item*3.281,1) for item in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[numeros for numeros in valores if numeros%2==0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[((items-32)*5/9)for items in temperatura_fahrenheit]
print(grados_celsius)


if(5>3):
    print('hoka')