import matplotlib.pyplot as plt
import numpy as np

fechas = ['19/08/2019', '20/08/2019', '21/08/2019', '22/08/2019', '23/08/2019']
primas = [79, 80, 79, 80, 82]
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
plt.barh(range(5), primas, edgecolor='white', linewidth="1.5", color="yellow")
#Fechas rotadas 60 grados
# plt.yticks(range(5), fechas, rotation=60)
plt.yticks(range(5), fechas)
plt.title("PRIMA DE RIESGO EN ESPAÑA", color="yellow")
#xlim: Obtiene o establece los límites x de los ejes actuales.
plt.xlim(min(primas)-1, max(primas)+1)
plt.grid(linestyle="--")

#Formato de los ejes
plt.gca().tick_params(axis='x', labelsize =12, colors="lightgray",grid_color='lightgray',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="lightgray",grid_color='lightgray',length=6, width=2)

ax = plt.gca()
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

#Fondo del gráfico de color gris claro
plt.gca().patch.set_facecolor('xkcd:dark grey')
#Seteo la opacidad del fondo del grafico
plt.gca().patch.set_alpha(0.3)


paises = ("Alemania", "España", "Francia", "Portugal")
posicion_y = np.arange(len(paises))
unidades = (342, 321, 192, 402)
plt.subplot(1,2,2)
plt.barh(posicion_y, unidades, align = "center", edgecolor='white', linewidth="1.5", color="yellow")
plt.yticks(posicion_y, paises)
plt.xlabel('Unidades vendidas', color="yellow")
plt.title("Ventas en Europa", color="yellow")
plt.grid(linestyle="--")

#Formato de los ejes
plt.gca().tick_params(axis='x', labelsize =12, colors="lightgray",grid_color='lightgray',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="lightgray",grid_color='lightgray',length=6, width=2)

ax = plt.gca()
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

#Fondo general de color gris oscuro
plt.figure(1).patch.set_facecolor('xkcd:black')
plt.figure(1).patch.set_alpha(0.70)
#Fondo del gráfico de color gris oscuro
plt.gca().patch.set_facecolor('xkcd:dark grey')
#Seteo la opacidad del fondo del grafico
plt.gca().patch.set_alpha(0.3)

#ajustar la distancia entre subgraficas
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.show()