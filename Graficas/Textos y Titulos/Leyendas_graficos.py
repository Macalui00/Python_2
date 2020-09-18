#Añadir leyendas a un gráfico
#Para añadir leyendas al gráfico anterior asignar al parámetro "label=" de plot() el literal de la leyenda a mostrar. Y después, ejecutar el método legend().

import matplotlib.pyplot as plt

lista1 = [11,2,3,15,8,13,21,34]
lista2 = [2,3,4,2,3,6,4,10]
lista3 = [9,15,9,15,9,15,9,15]

plt.plot(lista1, label = "Enero")
plt.plot(lista2, label = "Febrero")
plt.plot(lista3, label = "Marzo")
# plt.legend()

#Puedo indicar la posicion de las leyendas (loc=):
# upper, arriba
# lower, abajo
# center, centro
# left, izquierda y 
# right, derecha

#Ejemplo:
plt.legend(loc="upper left") 
plt.show()