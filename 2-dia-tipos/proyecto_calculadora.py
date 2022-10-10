nombre=input("Ingrese su nombre: ")
ventas=input("Ingrese sus ventas: ")
comision=round(float(ventas)*0.13,2)



print("------Resultado---------")
print(f"Bienvenido Sr. {nombre},")
print(f"Usted ha realizado un total de ventas de: {ventas}")
print(f"Su comisión es de: {comision}")

print("------Fin Resultado---------")