# Gráfico de caja y bigotes o boxplot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'

jap = np.random.uniform(166, 176, 100)
ale = np.random.uniform(175, 185, 100)
arg = np.random.uniform(170, 180, 100)

plt.figure(figsize=(10,7))
# Cambio los colores para que se vea bien en VSC con tema oscura
plt.boxplot([jap, ale, arg],
            #Hacer que la caja tenga silueta en la media:
            notch=True,
            #La caja sea rellena:
            patch_artist=True,
            #Formato de la caja:
            #Facecolor: relleno, Color: borde, Alpha: opacidad
            boxprops=dict(facecolor="lightpink", color="lightpink",alpha=0.5),
            #limite superior e inferior:
            capprops=dict(linewidth=2, color="magenta",alpha=0.4),
            #mediana:
            medianprops=dict(linewidth=2, color="orange",alpha=0.4),
            #Lineas verticales:
            whiskerprops=dict(linestyle='--', linewidth=2, color="pink"))

plt.xticks([1, 2, 3], ['Japón', 'Alemania', 'Argentina'])
#Le doy al titulo del grafico y de los ejes, color, formato y tamaño.
plt.xlabel('Paises', fontsize=14, fontweight='bold', color="darkgray")
plt.ylabel('Estaturas (cm)', fontsize=14, fontweight='bold', color="darkgray")
plt.title("Boxplot",fontsize=20, fontweight='bold', color="darkgray")
#Le doy formato a los ejes, color, rotacion, tamaño de letra. Length y Width me permite setear el grosor y tamaño de las marcas de los ejes.
plt.gca().tick_params(axis='x', rotation=30,labelsize =12, colors="darkgray",grid_color='darkgray',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="darkgray",grid_color='darkgray',length=6, width=2)


#Fondo general de color gris oscuro
plt.figure(1).patch.set_facecolor('xkcd:dark grey')
#Fondo del gráfico de color gris claro
plt.gca().patch.set_facecolor('xkcd:light grey')
#Seteo la opacidad del fondo del grafico
plt.gca().patch.set_alpha(0.3)

ax = plt.axes()

#Seteo el grosor de los ejes:
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
#Seteo el color de los ejes:
ax.spines['bottom'].set_color("darkgray")
ax.spines['left'].set_color("darkgray")
ax.spines['top'].set_color("darkgray")
ax.spines['right'].set_color("darkgray")
#Puedo setear la visibilidad de los ejes:
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()
#Mostrar el gráficp
plt.show()

#https://nataliaacevedo.com/tipos-de-graficos-en-python-con-matplotlib/