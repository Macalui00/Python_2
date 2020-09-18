import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd

# x = [1, 2, 3]
# y = [2, 4, 6]

# a=np.linspace(0,5,100)

# figure, axes = plt.subplots(nrows=2, ncols=2)

# constrained_layout ajusta automáticamente las subtramas y decoraciones para que encajen en la figura, de la mejor manera posible.
# constrained_layout debe ser activado antes o durante la creación de la subparcela ya que optimiza la disposición antes de cada paso del dibujo.
# figure, axes = plt.subplots(2,2, constrained_layout=True)

# #Grafica 1
# axes[0, 0].plot(x, y) 
# #Grafica 2,3 y 4
# axes[0, 1].plot(a, np.sin(a))
# axes[1, 0].plot(a, np.cos(a))
# axes[1, 1].plot(range(10))

# axes[0, 0].set_title("subplot 1")

# axes[0, 1].set_title("subplot 2")
# axes[1, 0].set_title("subplot 3")
# axes[1, 1].set_title("subplot 4")

# figure.tight_layout() #mantiene automáticamente el espacio correcto entre las subtramas.
# #Si no usamos el método tight_layout(), una fila se superpondrá con el título de la siguiente.

#Otra manera diferente de hacer esto ultimo:
# plt.subplots_adjust(left=0.125, #sirve para cambiar el espacio entre los subtramas.
#                     bottom=0.1, 
#                     right=0.9, 
#                     top=0.9, 
#                     wspace=0.2, 
#                     hspace=0.35)

fig = plt.figure()
plt.subplot(221)

#subplot_tool: Este método lanza una ventana de herramientas de subtrama para una figura.
plt.imshow(rnd.random((100, 100)))
plt.subplot(222)
plt.imshow(rnd.random((100, 100)))
plt.subplot(223)
plt.imshow(rnd.random((100, 100)))
plt.subplot(224)
plt.imshow(rnd.random((100, 100))) 
plt.subplot_tool()

plt.show()


#https://www.delftstack.com/es/howto/matplotlib/how-to-improve-subplot-size-or-spacing-with-many-subplots-in-matplotlib/