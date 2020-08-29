#Dadas estas dos listas:
l1 = [1,2,3,4]
l2 = [3,4,5,6]

#Obtengo una nueva lista que es la interseccion de las dos listas:
l3 = [num for num in l1 if num in l2]
print(l3)

#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]