def contar_primos(dato):
    lista_primos=[2,3]
    for item in range(2,dato+1):
        if item%2!=0 and item%3!=0 and item%4!=0 and item%5!=0 and item%6!=0 and item%7!=0 and item%8!=0 and item%9!=0:
            lista_primos.append(item)
    print(lista_primos)
    return len(lista_primos)

resultado = contar_primos(2)
print(resultado)