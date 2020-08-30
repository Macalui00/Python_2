"""Generadores:
Los generadores son iteradores.
Los generadores pueden ser creador con funciones generadoras.
Funciones generadores usan la palabra clave yield.
Los generadores pueden ser creados con expresiones generadoras.
"""

"""
FUNCIONES VS FUNCIONES GENERADORAS:
Funciones                                       | Funcion generadora
------------------------------------------------------------------------------------------
usa return                                      | usa yield
podes retornar 1 sola vez                       | podes rendir(yield) multiples veces
Cuando es invocada, retorna el valor de retorno | cuando es invocada, retorna un generador
"""

#Vayamos a un ejemplo:
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

generador = count_up_to(5)
print(generador) #objeto generador
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#Entonces esta es otra alternativa de crear un iterador, en vez de, crear un objeto, acá creamos una funcion que retorna un objeto generador.
print(help(generador))

generador = count_up_to(10)
lista = list(generador)
print(lista)