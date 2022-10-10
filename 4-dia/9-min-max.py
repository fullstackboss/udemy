menor=min(58,12,66,36,10,78,99)
mayor=max(58,12,66,36,10,78,99)
print(menor)
print(mayor)


"""En una lista"""
lista = [2,4,6,8,50,9,22,45,6,78,95]
print(min(lista))
print(max(lista))

"""con string"""
lista_string=["karlos","ivan","hugo","sergo"]
print(min(lista_string))

nombre="zigato"
print(min(nombre.lower()))

"""Con colecciones"""
dic={'C1':45,"C2":6}
print(min(dic.values()))

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima=min(diccionario_edades.values())
ultimo_nombre=max(diccionario_edades)
print(edad_minima)
print(ultimo_nombre)