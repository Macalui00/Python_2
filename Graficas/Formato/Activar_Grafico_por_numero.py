import matplotlib.pyplot as plt
import numpy as np

lista1 = [11,2,3,15,8,13,21,34]
lista2 = [2,3,4,2,3,6,4,10]
lista3 = [9,15,9,15,9,15,9,15]

plt.figure()   #  Añade un nuevo gráfico y lo activa
plt.plot(lista1, lista2, "r")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafico 1")
plt.figure(1)   # Activa el gráfico 1
plt.show()

plt.figure() 
plt.plot(lista2, lista3, "r")
plt.xlabel("x")
plt.ylabel("y")
plt.figure(1)   # Activa el gráfico 2
plt.show()