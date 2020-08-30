"""Iterators VS Iterables:
Un Iterador es un objeto sobre el que se puede iterar. Un objeto que retorna datos, un elemento a la vez en el momento en que se llama a next()
Un Iterable es un objeto que retornará un iterador cuando iter() es llamado.

Ok, pero que significa todo esto realmente?

El string "HELLO" es un iterable pero no un iterador porque si llamo iter(HELLO) retorna un iterador."""

name = "Oprah"
# next(name) #tira un error indicando que es un objeto string y no es un iterador.

print(iter(name))

it = iter(name)

"""Cuando next() es llamado en un iterador, el iterador retorna el siguiente elemento. Sigue haciendolo hasta que salte un error de StopIteration"""

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) #Tira error

#Podemos hacer lo mismo con una lista de numeros:
numeros = [1,2,3,4,5]
it = iter(numeros)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) #Tira error