import numpy as np
import pylab as pl

#Creo dos arrays de 10 elementos
x = np.arange(1, 11)
y = np.random.randint(10, size=10)

# print(x, y)

#Creo una grafica lineal (plot) con un array como eje x y el otro como eje y
# pl.plot(x, y)
# #Lo muestro
# pl.show()

#Otra manera de hacer algo parecido pero esta vez con una sola lista de valores
lista1 = [11,2,3,15,8,13,21,34]   # Declara lista1 con 8 valores
pl.plot(lista1,color="yellow")   # Dibuja el gráfico
pl.title("Gráfica lineal", fontsize="18", color="yellow",fontweight="bold") # Establece el título del gráfico
pl.xlabel("abscisa", fontsize="15", fontweight="bold", color="yellow")   # Establece el título del eje x
pl.ylabel("ordenada", fontsize="15", fontweight="bold", color="yellow")   # Establece el título del eje y
#Formato de los ejes
pl.gca().tick_params(axis='x', labelsize =12, colors="lightgray",grid_color='lightgray',length=6, width=2)
pl.gca().tick_params(axis='y', labelsize =12, colors="lightgray",grid_color='lightgray',length=6, width=2)

#Fondo general de color negro
pl.figure(1).patch.set_facecolor('xkcd:black')
#Fondo del gráfico de color gris claro
pl.gca().patch.set_facecolor('xkcd:light grey')
#Seteo la opacidad del fondo del grafico
pl.gca().patch.set_alpha(0.3)

ax = pl.axes()

#Seteo el grosor de los ejes:
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)

#Seteo el color de los ejes:
ax.spines['bottom'].set_color("lightgray")
ax.spines['left'].set_color("lightgray")
ax.spines['top'].set_color("lightgray")
ax.spines['right'].set_color("lightgray")

#Ajustar el tamaño de la ventana al grafico
pl.figure(1).tight_layout()

pl.show()