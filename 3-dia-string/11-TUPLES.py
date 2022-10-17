mituple=(1,2,3,4,6)
mituple=('hola',2.5,[10,2,5],'eve',6)
mituple='hola',2.5,[10,2,5],'eve',6
print(mituple[2][2])

"""Los tuple no pueden cambiarse - SON A PRUEBA DE DAÑOS"""

tuple=(8,9,(1,2,3),9)
print(tuple[2][1])
neotuple=list(tuple)
print(type(neotuple))
print(neotuple)

"""Asignaciones : Deben tener la mosca cantidad de elementos"""
t=1,2,3
x,y,z=t
print(x,y,z)

"""----COUNT: Contar elementos dentro del tuple"""
tu=1,2,3,4,1,1,2,1,(1,1,2)
print(tu.count(1))

"""----INDEX: Indice se encuentra"""
tu=1,2,3,4,1,1,2,1,(1,1,2)
print(tu.index(4))