"""Este es el juego piedra, papel o tijera, donde pueden jugar 2 personas y gana el mejor de 3 rondas."""

#Imprimo por consola una breve intro al juego
print("""Piedra...
Papel...
Tijeras....

Serán 3 rondas.
Por favor ingrese su jugada con las siguientes palabras:
Piedra, Papel, Tijeras. ¡Respetando las mayusculas!

""")

def chequearJugada(jugador, n):
    """Me permite verificar si la jugada insertada por el jugador es correcta"""
    while (jugador != "Piedra" and jugador != "Papel" and jugador != "Tijeras"):
        jugador = input(f"Jugador {n} ingrese su jugada:")
    return jugador

def obtenerJugadas():
    """Obtengo la jugada de cada jugador"""
    n = 1
    jugador1 = input(f"Jugador {n} ingrese su jugada:")
    jugador1 = chequearJugada(jugador1, n)
    n = 2
    jugador2 = input(f"Jugador {n} ingrese su jugada:")
    jugador2 = chequearJugada(jugador2, n)
    return jugador1,jugador2

def obtenerGanador(jugador1,jugador2, partida, puntajeJug1, puntajeJug2):
    """Obtengo el ganador de la ronda"""
    if (jugador1 == "Piedra" and jugador2 == "Papel") or (jugador1 == "Tijeras" and jugador2 == "Piedra") or (jugador1 == "Papel" and jugador2 == "Tijeras"):
        puntajeJug2 = puntajeJug2 + 1
        print(f"La partida {partida} la ganó jugador 2, su puntaje ahora es de: {puntajeJug2}")
    elif (jugador1 == "Piedra" and jugador2 == "Piedra") or (jugador1 == "Papel" and jugador2 == "Papel") or (jugador1 == "Tijeras" and jugador2 == "Tijeras") :
        puntajeJug2 = puntajeJug2 + 1
        puntajeJug1 = puntajeJug1 + 1
        print(f"Ha habido un empate! Jugador 1 {puntajeJug1} - {puntajeJug2} Jugador 2")
    else:
        puntajeJug1 = puntajeJug1 + 1
        print(f"La partida {partida} la ganó jugador 1, su puntaje ahora es de: {puntajeJug1}")
    return puntajeJug1, puntajeJug2

#Inicializo la partida y los puntajes de los jugadores
partida = 1
puntajeJug1 = 0
puntajeJug2 = 0

#Realizo 3 rondas donde se va incrementando el puntaje y el numero de ronda (partida)
while partida < 4:
    jugador1,jugador2 = obtenerJugadas()
    puntajeJug1, puntajeJug2 = obtenerGanador(jugador1,jugador2, partida, puntajeJug1, puntajeJug2)
    partida = partida + 1
#Determino quien ganó el juego:
if puntajeJug1 > puntajeJug2:
    print("Jugador 1 gano!!")
else:
    print("Jugador 2 gano!!")

