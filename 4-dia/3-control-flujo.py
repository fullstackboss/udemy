if 10>8:
    print('es correcto')
else:
    print('es incorrecto')

"""
x=True
if x:
    print('es correcto')
"""

mascota=input("ingresa animal: ")
if mascota == 'gato':
    print('tienes un gato')
elif mascota=='perro':
    print('tienes un perro')
else:
    print('no se que animal tienes')

edad=16
calificacion=5
if (edad<18):
    print('eres menor')
    if calificacion>7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('eres adulto')

"""ACTUALIZACION PYTHON 3.10"""

nombre="vegeta"
match nombre:
    case "vegeta":
        print("principe saiya")
    case "kakaroto":
        print ("guerrero menor")
    case "broly":
        print("guerrero legendario")
    case _:
        print("Guerero desconocido")




"""Estructura por patrones"""
cliente = {'nombre':'federico',
           'edad':45,
           'ocupacion':'webero'
           }
pelicula = {'titulo':'Matrix',
            'ficha_tecnica': {'protagonista':'keanureeves', 'director':'lanay lilly'}}

elementos =[cliente, pelicula, 'libro']

for item in elementos:
    match item:
        case{'nombre':nombre,
             'edad':edad,
             'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre,edad, ocupacion)
        case {'titulo':titulo,
            'ficha_tecnica':{'protagonista':protagonista, 'director':director}}:
            print("es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("no se que es esto")
