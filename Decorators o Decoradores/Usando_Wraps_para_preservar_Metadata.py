"""PRESERVANDO METADATA"""
# def log_function_data(fn):
#     def wrapper(*args, **kwargs):
#         """I AM WRAPPER FUNCTION"""
#         print(f"you are about to call {fn.__name__}")
#         print(f"Here's the documentation: {fn.__doc__}")
#         return fn(*args, **kwargs)
#     return wrapper

# @log_function_data
# def add(x,y):
#     """Suma los dos argumentos."""
#     return x+y

# # print(add(10,30))
# #Si ejecutamos lo siguiente:
# print(add.__doc__)
# print(add.__name__)
# help(add)
#No nos da el add help que seteamos con el add docstring, entonces queda el docstring como i am wrapper function y el nombre cambia a wrapper
#Esto puede llegar a ser problematico especialmente si otra persona esta trabajando con nuestro codigo
#Probablemente, no quieras que esto suceda, afortunadamente para nosotros, Python ofrece una manera sencilla para preservar los metadatos:
#Existe un modulo llamado functools y de el hay algo llamado wraps:
"""
from functools import wraps

#wraps preserva la metadata de una funcion cuando es decorada (envuelta)
def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #do some stuff with fn(*args, **kwargs)
        pass
    return wrapper
"""
from functools import wraps

#AHORA ARREGLAMOS EL CODIGO:
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    """Suma los dos argumentos."""
    return x+y


#Ahora si ejecutamos lo siguiente:
print(add.__doc__)
print(add.__name__)
help(add)