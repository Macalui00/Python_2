# Gráfico de escaleras
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.step(x, y,color="yellow")
plt.title("Gráfico de escaleras", fontsize="18", color="yellow",fontweight="bold")

#Formato de los ejes
plt.gca().tick_params(axis='x', labelsize =12, colors="lightgray",grid_color='lightgray',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="lightgray",grid_color='lightgray',length=6, width=2)

#Fondo general de color negro
plt.figure(1).patch.set_facecolor('xkcd:black')
#Opacidad del fondo
plt.figure(1).patch.set_alpha(0.7)

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
ax.spines['bottom'].set_color("lightgray")
ax.spines['left'].set_color("lightgray")
ax.spines['top'].set_color("lightgray")
ax.spines['right'].set_color("lightgray")

plt.show()