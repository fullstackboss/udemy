texto_usuario=input("Ingrese texto:").lower()

lista_letras=[]

lista_letras.append(input("Ingrese la primera letra a buscar:").lower())
lista_letras.append(input("Ingrese la segunda letra a buscar:").lower())
lista_letras.append(input("Ingrese la tercera letra a buscar:").lower())


print("\n")
print("CANTIDAD DE LETRAS")
cant_letra_1=texto_usuario.count(lista_letras[0])
cant_letra_2=texto_usuario.count(lista_letras[1])
cant_letra_3=texto_usuario.count(lista_letras[2])




total_palabras=texto_usuario.split()
primera_letra=texto_usuario[0]
ultima_letra=texto_usuario[-1]
separa_palabras=total_palabras[::-1];
nuevo_orden=" ".join(separa_palabras)
encontrar_python='python' in texto_usuario

print("\n")
print("LETRAS ENCONTRADAS")
print(f"Numero de coincidencias de la letra '{lista_letras[0]}' es:", cant_letra_1)
print(f"Numero de coincidencias de la letra '{lista_letras[1]}' es:", cant_letra_2)
print(f"Numero de coincidencias de la letra '{lista_letras[2]}' es:", cant_letra_3)
print(f"Numero de palabras es:", len(total_palabras))
print(f"Primera letra es:", primera_letra)
print(f"Ultima letra es:", ultima_letra)
print("\n")
print("OTROS")
print(f"A la inversa es:", nuevo_orden)
print("\n")
print("SE ENCUENTRA PYTHON")
diccionario={'True':'Si esta la palabra','False':'no se encuentra'}
decicion=str(encontrar_python)
print(f"La palabra python: ", diccionario[decicion])






