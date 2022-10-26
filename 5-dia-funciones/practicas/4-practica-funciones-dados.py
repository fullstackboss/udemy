from random import *
def lanzar_dados():
    dado1=''
    dado2 = ''
    for elemento in range(1,3):
        dado1=randint(1,6)
        dado2 = randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dato1,dato2):
    respuesta=''
    suma_dados=dato1+dato2
    if (suma_dados<=6):
        respuesta=f"La suma de tus dados es {suma_dados}. Lamentable"
    elif (suma_dados>6) and (suma_dados<10):
        respuesta=f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        respuesta=f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    return respuesta


res1,res2=lanzar_dados()
print(f"Dado A: {res1} \nDado B: {res2}")
evaluar_jugada(res1,res2)

print(evaluar_jugada(res1,res2))
