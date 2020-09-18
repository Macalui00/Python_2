import matplotlib.pyplot as plt
import numpy as np

#Gráfico de series comparadas (fill_between)
for t in range(1, 11)[::-1]:
    plt.fill_between(
        range(1, 11),
        [t * n for n in range(1, 11)],
        label=f"Tabla del {t}"
    )
plt.title("Tablas de multiplicar", color="lightgray", fontsize=18,fontweight="bold")
plt.legend(loc='upper left')

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
plt.figure(1).patch.set_facecolor('xkcd:dark grey')
plt.figure(1).patch.set_alpha(0.70)
#Fondo del gráfico de color gris oscuro
plt.gca().patch.set_facecolor('xkcd:light grey')
#Seteo la opacidad del fondo del grafico
plt.gca().patch.set_alpha(0.3)

plt.show()

"""Lo de [::-1] es un "truco" frecuentemente usado en python para obtener una lista o una cadena "del revés". Se basa en el operador slice (rodaja) cuya sintaxis general es:

iterable[inicio:fin:paso]
que permite extraer una serie de elementos del iterable, comenzando por el numerado como inicio y terminando por el numerado como fin-1, aumentando de paso en paso.

Si omites inicio se empezará en el primer elemento del iterable, si omites fin se terminará en el último elemento del iterable.

Si el paso es negativo, el iterable se recorre "hacia atrás", y en ese caso los valores por defecto cuando se omite inicio y fin se invierten.

Así pues iterable[::-1] devuelve los elementos del iterable, comenzando por el último y terminando por el primero, en orden inverso a como estaban."""