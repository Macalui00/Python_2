"""En la leccion anterior vimos que las funciones que son envueltas no contienen argumentos, en este veremos como utilizar esos argumentos de las funciones envueltas
"""
#Corregimos el error de los parametros
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# @shout
# def greet(name):
#     return f"Hi, I'm {name}"

# @shout
# def order(main, side):
#     return f"Hi, I'd like the {main}, with a side of {side}, please"

# print(greet("todd"))
# print(order("burger", "fries")) #Esto retorna un error: wrapper() takes 1 positional argument but 2 were given

""" PARA CORREGIR ESTE ERROR:
def my_decorator(fn):
    def wrapper(*arg, **kwargs):
        #do some stuff with fn(*args, **kwargs)
        pass
    return wrapper
"""

#correccion
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}"

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please"

@shout
def lol():
    return "lol"
#Ahora probemos si funciona:
print(greet("todd"))
# print(order("burger", "fries"))
print(order(side = "burger", main = "fries"))
print(lol())