from functools import wraps

def doble_retorno(fn):
    """Se llama a la funcion pasandole una funcion y la misma es realizada dos veces y esos resultados se devuelven en una lista"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val,val]
    return wrapper

@doble_retorno
def add(x, y):
    return x + y
    
print(add(1, 2)) # [3, 3]

@doble_retorno
def greet(name):
    return "Hi, I'm " + name

print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]