"""Este es el juego piedra, papel o tijera, donde un jugador juega contra la computadora y gana el mejor de 3 rondas."""
import random

#Imprimo por consola una breve intro al juego
print("""Piedra...
Papel...
Tijeras....

Serán 3 rondas.
Por favor ingrese su jugada con las siguientes palabras:
Piedra, Papel, Tijeras. ¡Respetando las mayusculas!

""")

def chequearJugada(jugador):
    """Me permite verificar si la jugada insertada por el jugador es correcta"""
    while (jugador != "Piedra" and jugador != "Papel" and jugador != "Tijeras"):
        jugador = input(f"Ingrese su jugada:")
    return jugador

def jugadaRandom(jugadas):
    """Obtenemos la jugada hecha por la computadora de manera aleatoria"""
    numero = random.randint(0, 2)
    jugadaComputadora = jugadas[numero]
    return jugadaComputadora   

def obtenerJugadas(jugadas):
    """Obtengo la jugada del jugador y de la computadora"""
    jugador1 = input(f"Ingrese su jugada:")
    jugador1 = chequearJugada(jugador1)
    jugadorCompu = jugadaRandom(jugadas)
    print(f"La computadora ha hecho la siguiente jugada: {jugadorCompu}")
    return jugador1,jugadorCompu
    
def obtenerGanador(jugador1,jugador2, partida, puntajeJug1, puntajeJug2):
    """Obtengo el ganador de la ronda"""
    if (jugador1 == "Piedra" and jugador2 == "Papel") or (jugador1 == "Tijeras" and jugador2 == "Piedra") or (jugador1 == "Papel" and jugador2 == "Tijeras"):
        puntajeJug2 = puntajeJug2 + 1
        print(f"La partida {partida} la ganó la computadora, su puntaje ahora es de: {puntajeJug2}")
    elif (jugador1 == "Piedra" and jugador2 == "Piedra") or (jugador1 == "Papel" and jugador2 == "Papel") or (jugador1 == "Tijeras" and jugador2 == "Tijeras") :
        puntajeJug2 = puntajeJug2 + 1
        puntajeJug1 = puntajeJug1 + 1
        print(f"Ha habido un empate! Jugador {puntajeJug1} - {puntajeJug2} Computadora")
    else:   
        puntajeJug1 = puntajeJug1 + 1
        print(f"La partida {partida} la ganó jugador 1, su puntaje ahora es de: {puntajeJug1}")
    return puntajeJug1, puntajeJug2

#Inicializo las variables
partida = 1
puntajeJug1 = 0
puntajeJugCompu = 0
jugadas = ["Piedra", "Papel", "Tijeras"]

#Se realizan las 3 rondas
while partida < 4:
    jugador1,jugadorCompu = obtenerJugadas(jugadas)
    puntajeJug1, puntajeJugCompu = obtenerGanador(jugador1,jugadorCompu, partida, puntajeJug1, puntajeJugCompu)
    partida = partida + 1
#Determino quien gana:
if puntajeJug1 > puntajeJugCompu:
    print("Has ganado!!")
else:
    print("Mala suerte, la compu te gano!!")

