#Listas por comprension con logica condicional:

numeros = [1,2,3,4,5,6]

#Guardo en la lista aquellos numeros que sean pares:
pares = [num for num in numeros if num % 2 == 0]

#Guardo en la lista aquellos numeros que sean impares:
impares = [num for num in numeros if num % 2 != 0]

#Si son pares que se los multiplique por 2 y sino, que se los divida por 2
print([num*2 if num % 2 == 0 else num/2 for num in numeros])

listaConVocales = "Esto es muuy divertido!"

print("".join(char for char in listaConVocales if char not in "aeiou"))

print("".join(["cool", "dude"]))
print("...".join(["cool", "dude"]))

#Para obtener la primera letra de cada nombre:
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
print(answer)

#Misma manera de hacer esto ultimo pero con loops
answerV2 = []
for person in ["Elie", "Tim", "Matt"]:
    answerV2.append(person[0])
print(answerV2)