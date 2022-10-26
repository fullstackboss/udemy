def devolver_distintos(v1,v2,v3):
    lista=[v1,v2,v3]
    mayor=max(lista)
    menor=min(lista)
    for item in lista:
        if (item!=mayor and item!=menor):
            intermedio=item
    respuesta=''
    if sum(lista)>15:
        respuesta=mayor
    elif sum(lista)<10:
        respuesta=menor
    elif sum(lista) >= 10 or sum(lista)<=15:
        respuesta=intermedio
    return respuesta

print(devolver_distintos(3,2,7))


