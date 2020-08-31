"""Doctests:
Podemos escribir testeos para funciones dentro del docstring
Escribir codiga que parece estar dentro de un REPL"""

#Ejemplo de Doctests
"""suma x e y

>>>add(1,2)
3

>>>add(8,"hi")
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +: "int" and "str"
"""

# def add(a,b): 
#     """
#     >>> add(2,3)
#     5
#     >>> add(100,200)
#     300
#     """
#     return a * b #Tirará error

#Para ejecutar el doctest por consola:
#python -m doctest -v Doctests.py
def add(a,b): 
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    return a + b #No tirará error

def double(values):
    """Dobla los valores en una lista

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: "int" and "NoneType"
    """
    return [2 * element for element in values]
    #En el ultimo estamos escribiendo algo que no va a funcionar, Y si queremos testearlo para asegurarnos de que obtendremos un error... 
def say_hi():
    """
    >>> say_hi()
    "hi"
    """
    return "hi"

def true_that():
    """
    >>> true_that()
    True
    """
    return True

def make_dict(keys):
    """
    >>> make_dict(['a','b'])
    {'b': True, 'a': True}
    """
    return {key: True for key in keys}

"""ISSUES CON DOCTESTS
La sintaxis es un poco extraña
Desordena nuestro código de función
Carece de muchas caracteristicas de las herramientas de prueba más grandes
Los testeos pueden llegar a ser frágiles"""