#Listas por comprension:

nums = [1,2,3]
print([x*10 for x in nums])

#Listas por comprension VS loops:
numeros = [1,2,3,4,5]
doble_numeros = []

def duplicarNumerosFor(numeros):
    """Duplico cada elemento de la lista mediante un loop for"""
    for num in numeros:
        numero_doble = num * 2
        doble_numeros.append(numero_doble)
    print(doble_numeros)

#Claramente este caso es más simple y legible
def duplicarNumerosLC(numeros):
    """Duplico cada elemento de la lista mediante listas por comprension"""
    doble_numeros = [num*2 for num in numeros]
    print(doble_numeros)

nombre = "macarena"
print([char.upper() for char in nombre])

#multiplico por 10 cada uno de los elementos en el rango
print([num*10 for num in range(1,6)])
#Se castean a valores booleanos
print([bool(val) for val in [0,[],""]])

#Convierto una lista de numeros en una lista de strings
string_list = [str(num) for num in numeros]
print(string_list)