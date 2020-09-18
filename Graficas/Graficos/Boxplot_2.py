import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib import rcParams

rcParams['font.family'] = 'Comic Sans MS'

# Fixing random state for reproducibility
np.random.seed(19680801)

# Inventando alguna data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))

#Dos filas, 3 columnas:
fig, axs = plt.subplots(2, 3, figsize=(10,7))
# boxplot básico
axs[0, 0].boxplot(data)
axs[0, 0].set_title('boxplot básico',fontweight="bold")

# notched plot
axs[0, 1].boxplot(data, 1)
axs[0, 1].set_title('notched boxplot',fontweight="bold")

# Cambiando los simbolos de los elementos alejados
axs[0, 2].boxplot(data, 0, 'gD')
axs[0, 2].set_title('cambiando simbolos\nde elementos alejados',fontweight="bold")

# no mostrar elementos salientes
axs[1, 0].boxplot(data, 0, '')
axs[1, 0].set_title("no mostrar\nelementos salientes",fontweight="bold")

# cajas horizontales
axs[1, 1].boxplot(data, 0, 'rs', 0)
axs[1, 1].set_title('cajas horizontales', fontweight="bold")


# Cambiar el tamaño del bigote
axs[1, 2].boxplot(data, 0, 'rs', 0, 0.95)
axs[1, 2].set_title('cambiar el tamaño\ndel bigote',fontweight="bold")

#Ajustando el tamaño de cada subplot
fig.subplots_adjust(left=0.10, right=0.80, bottom=0.05, top=0.9,
                    hspace=0.5, wspace=0.5)

for n in range(0,2):
    for m in range(0,3):
        #Fondo del gráfico de color gris oscuro
        axs[n, m].patch.set_facecolor('xkcd:dark grey')
        #Seteo la opacidad del fondo del grafico
        # axs[1, 0].patch.set_alpha(0.9)
        #Seteo el grosor de los ejes:
        axs[n, m].spines['bottom'].set_linewidth(1.5)
        axs[n, m].spines['left'].set_linewidth(1.5)
        axs[n, m].spines['top'].set_linewidth(1.5)
        axs[n, m].spines['right'].set_linewidth(1.5)
        #Seteo el color de los ejes:
        axs[n, m].spines['bottom'].set_color("black")
        axs[n, m].spines['left'].set_color("black")
        axs[n, m].spines['top'].set_color("black")
        axs[n, m].spines['right'].set_color("black")
        #Formato de los ejes
        axs[n, m].tick_params(axis='x', labelsize =12, colors="black",grid_color='black',length=6, width=2)
        axs[n, m].tick_params(axis='y', labelsize =12, colors="black",grid_color='black',length=6, width=2)


# inventando más datos
spread = np.random.rand(50) * 100
center = np.ones(25) * 40
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
d2 = np.concatenate((spread, center, flier_high, flier_low))
# Making a 2-D array only works if all the columns are the
# same length.  If they are not, then use a list instead.
# This is actually more efficient because boxplot converts
# a 2-D array into a list of vectors internally anyway.
data = [data, d2, d2[::2]]

# Multiple box plots on one Axes
fig, ax = plt.subplots()
ax.boxplot(data)
plt.title("Ejemplo boxplot 2",fontweight="bold")

#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()
plt.figure(2).tight_layout()

#Fondo general de color amarillo
plt.figure(1).patch.set_facecolor('xkcd:yellow')
plt.figure(1).patch.set_alpha(0.9)
plt.figure(2).patch.set_facecolor('xkcd:yellow')
plt.figure(2).patch.set_alpha(0.9)

ax = plt.gca()
#Seteo el grosor de los ejes:
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
#Seteo el color de los ejes:
ax.spines['bottom'].set_color("black")
ax.spines['left'].set_color("black")
ax.spines['top'].set_color("black")
ax.spines['right'].set_color("black")
#Formato de los ejes
plt.gca().tick_params(axis='x', labelsize =12, colors="black",grid_color='black',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="black",grid_color='black',length=6, width=2)

#Fondo del gráfico de color gris oscuro
plt.gca().patch.set_facecolor('xkcd:dark grey')
#Seteo la opacidad del fondo del grafico
# plt.gca().patch.set_alpha()

#ajustar la distancia entre subgraficas
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.show()