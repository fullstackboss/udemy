"""--SETS:
- Elementos unicos: no se repiten.
- No estan ordenados en indice
- Son elementos inmutables
- No se incluyen listas o diccionarios
- Se requiere un solo argumento..por eso se encierra con []{}()

set(....) o {.....}
--"""

miset=set([1,2,3,4,5,6])
misetconllave=set({1,2,3,4,5,6})
misetconparetesis=set((1,2,3,4,5,6))
print(type(miset))
print(miset)
print(misetconllave)
print(misetconparetesis)

otroset={1,2,3}
print(type(otroset))

misetcontuple=set((1,2,(3,4,5),6))
print(misetcontuple)

""" calcula len"""
print(len(misetcontuple))

"""Busca"""
print(6 in misetcontuple)

"""---UNION de set---"""
s1={1,2,3}
s2={3,5,6}
s3=s1.union(s2)
print(s3)

"""---ADD de set---"""
set1={1,2,3}
set1.add(4)
print(set1)

"""---REMOVE de set---"""
set2={1,2,3,4,5,6,7,8,9,0}
set2.remove(3)
print(set2)

"""---DISCARD: descarta un elemento del set---"""
set2={1,2,3,4,5,6,7,8,9,0}
set2.discard(3)
print(set2)

"""---POP: elimina un elemento aleatorio del set---"""
set3={45,0,50,3,4,22,6,7}
sorteo=set3.pop()
print(sorteo)

