texto_usuario=input("Ingrese texto:").lower()

letra_buscar=input("Ingrese letra a buscar:")
total_palabras=texto_usuario.split()
primera_letra=texto_usuario[0]
ultima_letra=texto_usuario[-1]
inverse_orden=texto_usuario[::-1]

encontrar_python='python' in texto_usuario

print(f"Numero de coincidencias de la letra '{letra_buscar}' es:", texto_usuario.count(letra_buscar))
print(f"Numero de palabras es:", len(total_palabras))
print(f"Primera letra es:", primera_letra)
print(f"Ultima letra es:", ultima_letra)
print(f"A la inversa es:", inverse_orden)
print(encontrar_python)


