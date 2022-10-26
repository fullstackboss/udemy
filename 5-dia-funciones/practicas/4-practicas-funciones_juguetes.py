mis_animes={('goku',802),('akira',550),('hunterx',350), ('metalgear',128),('patlabor',80)}
mis_productos={('gundam',1082),('macross',150),('eva',250), ('transformes',458),('funko',120)}
#saber cual es el mas caro

def mas_caro(lista):
    precio_caro=0
    nom_tipo=''
    for tipo,precio in lista:
        if precio>precio_caro:
            precio_caro=precio
            nom_tipo=tipo
        else:
            pass
    return nom_tipo, precio_caro

nom,pre=mas_caro(mis_productos)
print(f"El producto mas caro es del tipo {nom} cuyo precio es de {pre}")

nom2,pre2=mas_caro(mis_animes)
print(f"El producto mas caro es del tipo {nom2} cuyo precio es de {pre2}")