#Listas anidadas:
listaAnidada = [[1,2,3],[4,5,6],[7,8,9]]

#Acceder a elementos de las listas anidadas:
print(listaAnidada[0][1])
print(listaAnidada[1][-1])

#Iterar elementos de la lista:
for l in listaAnidada:
    for val in l:
        print(val)