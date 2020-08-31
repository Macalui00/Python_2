from functools import wraps

"""Escribir una funcion que acepte una funcion y retorne otra funcion. La funcion pasada debe ser unicamente invocada si tiene menos de 3 argumentos. Caso contario, the inner function debe retornar MUCHOS ARGUMENTOS!"""

def menosDe3Args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        else:
            return "Demasiados argumentos!"
    return wrapper

@menosDe3Args
def add_all(*nums):
    return sum(nums)

print(add_all()) # 0
print(add_all(1)) # 1
print(add_all(1,2)) # 3
print(add_all(1,2,3)) # "Demasiados argumentos!"
print(add_all(1,2,3,4,5,6)) # "Demasiados argumentos!"