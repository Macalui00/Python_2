import matplotlib.pyplot as plt
import numpy as np

#Divido la ventana en 1 fila x 2 columnas y dibujo el primer gráfico
plt.subplot(1,2,1)
plt.plot((1,2,3,4,5,6,7,8,9,10))

#Divido la ventana en 1 fila x 2 columnas y dibujo el segundo gráfico
plt.subplot(1,2,2)
plt.plot((5,4,3,2,1))

#CASO CUATRO GRAFICAS:
plt.subplot(2,2,1)
plt.plot((1,2,3,4,5))
plt.subplot(2,2,2)
plt.plot((5,4,3,2,1))
plt.subplot(2,2,3)
plt.plot((1,2,3,4,5))
plt.subplot(2,2,4)
plt.plot((5,4,3,2,1))

#TRES GRAFICOS SOLOS
sample_data = np.random.normal(0, 0.1, 1000)
x = np.arange(1, 11)
y = np.random.randint(10, size=10)

#caso stem
plt.subplot(2,2,1)
plt.stem(x, y)
plt.title("Stem")

#caso histograma
plt.subplot(2,2,2)
plt.hist(sample_data, rwidth=0.9) #Separacion entre barras rwidth
plt.title("Histograma")

#Definimos una lista con paises como string
paises = ['Estados Unidos', 'España', 'Mexico', 'Rusia', 'Japon']
#Definimos una lista con ventas como entero
ventas = [25, 32, 34, 20, 25]
 
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.subplot(2,2,(3,4))
plt.bar(paises, ventas)
plt.title("Cantidad de ventas por pais")
plt.xlabel("Pais")
plt.ylabel("Ventas")
plt.subplots_adjust(wspace=0.5, hspace=0.5)

#Una forma de generar espacio entre graficos.
# You can use plt.subplots_adjust to change the spacing between the subplots (source)

# call signature:

# subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
# The parameter meanings (and suggested defaults) are:

# left  = 0.125  # the left side of the subplots of the figure
# right = 0.9    # the right side of the subplots of the figure
# bottom = 0.1   # the bottom of the subplots of the figure
# top = 0.9      # the top of the subplots of the figure
# wspace = 0.2   # the amount of width reserved for blank space between subplots
# hspace = 0.2   # the amount of height reserved for white space between subplots


#Otra manera de generar espacio entre gráficos.
fig, axes = plt.subplots(nrows=4, ncols=4)
fig.tight_layout() # Or equivalently,  "plt.tight_layout()"

plt.show()