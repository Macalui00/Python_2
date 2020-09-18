# Añadir rótulos a los ejes
# con el método figure() se representa sólo una lista de valores y se definen los rótulos de los ejes.

import matplotlib.pyplot as plt
import numpy as np

lista1 = [11,2,3,15,8,13,21,34]
lista2 = [2,3,4,2,3,6,4,10]
lista3 = [9,15,9,15,9,15,9,15]

plt.figure()  # Comenzamos un nuevo gráfico (figura)

#Dandole formato a la grafica
plt.title("Resultados")
plt.xlabel("Eje de abscisa")
plt.ylabel("Eje de ordenada")
plt.grid(True) 

indice = np.arange(8)   # Declara un array

#Los arrays se utilizan para definir los rótulos que se mostrarán en ambos ejes.
plt.xticks(indice, ("A", "B", "C", "D", "E", "F", "G", "H"))  
plt.yticks(np.arange(0,51,10))
plt.plot(lista1)

plt.show()