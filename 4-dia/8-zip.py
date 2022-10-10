nombres=['kakaroto','vegeta','cooler']
edades=[23,26,55]
union=list(zip(nombres,edades))
print(union)

origen=['tierra','vegeta','freserglobe']

union2=list(zip(nombres,edades,origen))
print(union2)

for nombres,edades,origen in union2:
    print(f"el guerrero {nombres} tiene una edad de {edades} y viene del planeta {origen}")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
union = list(zip(capitales, paises))
for capitales, paises in union:
    print(f"La capital de {paises} es {capitales}")

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))
print(numeros)








