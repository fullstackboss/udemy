monedas = 10
while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas -= 1
else:print("Ya no hay monedas")


respuesta='s'
while respuesta =='s':
    respuesta = input("Desea continua (s/n)")
    if respuesta == 'w':
        print("prohibido")

    if respuesta =='n':
        print("dijo que no")
        print("gracias")
        break
    continue

else:
    print("FIN")

