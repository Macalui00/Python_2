import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import load_dataset
from seaborn import lmplot

#Con este tipo de gráficos se puede ver la relación entre dos variables como puede ser la factura y la propina.

tips = load_dataset("tips")
tips.head()

#IMPORTANTE:https://stackoverflow.com/questions/23969619/plotting-with-seaborn-using-the-matplotlib-object-oriented-interface
# paleta = sns.color_palette("rocket_r", as_cmap=True)
# cmap = plt.get_cmap("YlOrBr")
# paleta = cmap(np.arange(start=1, stop=200, step=10)) 

sns.lmplot('total_bill', 'tip', data=tips, fit_reg=False, scatter_kws={"s": 100, "color":"white"})
plt.title("Sin linea de regresión lineal e\nintervalo de confianza", color= "white",fontweight="bold")
#Formato de los ejes
plt.gca().tick_params(axis='x', labelsize =12, colors="white",grid_color='white',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="white",grid_color='white',length=6, width=2)

#Seteo el grosor y color de los ejes:
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().set_xlabel('total_bill', color="white",fontweight="bold")
plt.gca().set_ylabel('tip', color="white",fontweight="bold")


#Fondo del gráfico de color gris claro
plt.gca().patch.set_facecolor('xkcd:light grey')
#Seteo la opacidad del fondo del grafico
plt.gca().patch.set_alpha(0.3)


lmplot('total_bill', 'tip', data=tips, scatter_kws={"s": 100, "color":"cyan", "alpha":0.4}, line_kws={"color":"darkcyan"})
plt.title("Con linea de regresión lineal e\nintervalo de confianza", color= "cyan",fontweight="bold")

#Formato de los ejes
plt.gca().tick_params(axis='x', labelsize =12, colors="cyan",grid_color='cyan',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="cyan",grid_color='cyan',length=6, width=2)

#Seteo el grosor y color de los ejes:
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().set_xlabel('total_bill', color="cyan",fontweight="bold")
plt.gca().set_ylabel('tip', color="cyan",fontweight="bold")
#Fondo del gráfico de color gris claro
plt.gca().patch.set_facecolor('xkcd:light grey')
#Seteo la opacidad del fondo del grafico
plt.gca().patch.set_alpha(0.3)

lmplot('total_bill', 'tip', data=tips, ci=None, scatter_kws={"s": 100, "color":"yellow", "alpha":0.4}, line_kws={"color":"white"})
plt.title("Con linea de regresión lineal\ny sin intervalo de confianza", color= "yellow",fontweight="bold")
#Fondo del gráfico de color gris claro
plt.gca().patch.set_facecolor('xkcd:light grey')
#Seteo la opacidad del fondo del grafico
plt.gca().patch.set_alpha(0.3)

#Formato de los ejes
plt.gca().tick_params(axis='x', labelsize =12, colors="yellow",grid_color='yellow',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="yellow",grid_color='yellow',length=6, width=2)

#Seteo el grosor y color de los ejes:
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().set_xlabel('total_bill', color="yellow",fontweight="bold")
plt.gca().set_ylabel('tip', color="yellow",fontweight="bold")

lmplot('total_bill', 'tip', data=tips,  hue="smoker", scatter_kws={"s": 100, "alpha":0.4}, palette="YlOrBr")
plt.title("Más de una regresión\nlineal a la vez", color= "orange",fontweight="bold")
#Fondo del gráfico de color gris claro
plt.gca().patch.set_facecolor('xkcd:light grey')
#Seteo la opacidad del fondo del grafico
plt.gca().patch.set_alpha(0.3)

#Formato de los ejes
plt.gca().tick_params(axis='x', labelsize =12, colors="orange",grid_color='orange',length=6, width=2)
plt.gca().tick_params(axis='y', labelsize =12, colors="orange",grid_color='orange',length=6, width=2)
plt.figure(4, figsize=(10,7))

#Seteo el grosor y color de los ejes:
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().set_xlabel('total_bill', color="orange",fontweight="bold")
plt.gca().set_ylabel('tip', color="orange",fontweight="bold")

#Fondo general de color gris oscuro
plt.figure(1).patch.set_facecolor('xkcd:dark grey')
plt.figure(2).patch.set_facecolor('xkcd:dark grey')
plt.figure(3).patch.set_facecolor('xkcd:dark grey')
plt.figure(4).patch.set_facecolor('xkcd:dark grey')

#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()
plt.figure(2).tight_layout()
plt.figure(3).tight_layout()
plt.figure(4).tight_layout()

plt.show()