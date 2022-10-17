diccionario={'c1':'valor1', 'c2':'valor2'}
print(diccionario)
resultado = diccionario['c2']
print(resultado)


cliente={'nombre':'alberto','apellido':'terrones', 'edad':45, 'peso':82.8}
print(cliente['nombre'])

"""Imprime en cierta ubicacion"""
dic={'c1':'kakaroto','c2':[20,30,50],'c3':{'v1':250,'v2':360,'v3':985}}
print(dic['c2'][2])
print(dic['c3']['v2'])

"""Ejercicio"""
dic2={'c1':['a','b','c'],'c2':['d','e','f']}
print((dic2['c2'][1]).upper())

"""Agregar elemento a diccionario"""
dic3={1:'a',2:'b'}


"""agrega elemento"""
dic3[3]='c'
print(dic3)

"""sobreescribe"""
dic3[2]='BB'
print(dic3)

"""Sobreescribe todas las claves"""
print(dic3.keys())

"""Sobreescribe todas los valores"""
print(dic3.values())

"""Sobreescribe todo"""
print(dic3.items())





