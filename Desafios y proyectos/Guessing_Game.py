import random

def chequearNumero(num):
    """Verifico si el numero ingresado esta entre 1 y 10"""
    while (num < 1 or num > 10):
        num = int(input("Numero erroneo, adivina el numero del 1 al 10:"))
    return num

def verificarRespuesta(resp):
    """Verifico si la respuesta dada por el usuario es correcta"""
    while resp != "si" and resp != "no":
        resp = input("¿Querés volver a intentarlo? si/no ")
    return resp

def obtenerRespuesta():
    """Verifico si el usuario realmente quiere seguir adivinando"""
    resp = input("¿Querés volver a intentarlo? si/no ")
    resp = verificarRespuesta(resp)
    return resp

def revisarNumero(numero):
    """Reviso si el usuario ha acertado el numero o no, y, si quiere continuar esperando"""
    num = int(input("Adivina el numero del 1 al 10:"))
    num = chequearNumero(num)
    if numero == num :
        print("¡Felicidades has acertado!")
        resp = "no"
    elif numero < num :
        print("Estas por arriba del numero")
        resp = obtenerRespuesta()
    else:
        print("Estas por debajo del numero")
        resp = obtenerRespuesta()
    if resp == "si":
        revisarNumero(numero)

def adivinaElNumero():
    """Funcion principal, donde se define el numero a adivinar y el usuario intenta adivinar cual es"""
    numero = random.randint(1, 10)
    revisarNumero(numero)

adivinaElNumero()