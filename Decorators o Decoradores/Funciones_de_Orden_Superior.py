from random import choice

#Podemos pasar funciones como argumentos en otras funciones:
def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(10,square))
print(sum(10,cube))

#Podemos anidar funciones dentro de otras:
def greet(person):
    def get_mood():
        msg = choice(("Hello there ", "Go away  ", "I love you "))
        return msg
    
    result = get_mood() + person
    return result

print(greet("Toby"))

#Podemos retornar funciones desde otras funciones:
def make_laught_func():
    def get_laugh():
        l = choice(("HAHAHAHAH", "lol", "tehehehe"))
        return l
    return get_laugh

laugh = make_laught_func()
print(laugh())

#Funciones anidadas pueden acceder al alcance de las funciones externas (outer function scope):
def make_laught_at_func(person):
    def get_laugh():
        laugh = choice(("HAHAHAHAH", "lol", "tehehehe"))
        return f"{laugh} {person}"
    return get_laugh

laugh_at = make_laught_at_func("linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())