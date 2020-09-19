import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import kdeplot
from seaborn import load_dataset

tips = load_dataset("tips")
tips.head()

#Los diagramas de densidad se pueden utilizar para ver cómo se comporta distribuciones de datos.
#En el conjunto de datos de ejemplo puede ser de interés comprobar cómo se distribuye los valores de la factura, para lo que se puede utilizar el siguiente ejemplo
fig, axes = plt.subplots(2, 3, figsize=(17,9))
fig.suptitle('Diagrama de densidad', color="orange",fontweight="bold",fontsize=18)
axes[0,0].set_title("Diagrama de una dimensión",color="orange",fontweight="bold",fontsize=14)
kdeplot(tips.total_bill, ax=axes[0,0], color="orange")

#Este tipo de gráficas también se puede obtener en dos dimensiones, para lo que solamente se ha de inyectar dos columnas de datos en la función
kdeplot(tips.tip,tips.total_bill, ax=axes[0,1], color="orange")
axes[0,1].set_title("Diagrama de dos dimensiones",color="orange",fontweight="bold",fontsize=14)

axes[0,1].set_xlabel('total_bill', color="orange",fontweight="bold",fontsize=14)
axes[0,1].set_ylabel('tip', color="orange",fontweight="bold",fontsize=14)

kdeplot(data=tips, y=tips.tip, ax=axes[0,2], color="orange")
axes[0,2].set_title("Diagrama eje y",color="orange",fontweight="bold",fontsize=14)
#Me tiraba este error: ValueError: could not convert string to float: 'Sun', indagando encontre lo siguiente: https://stackoverflow.com/questions/63827250/error-using-simple-kdeplot-example-from-the-doc
#Esto soluciono mi problema

iris = sns.load_dataset("iris")
sns.kdeplot(data=iris, ax=axes[1,0], palette="YlOrBr")
axes[1,0].set_title("Distribuciones por cada\ncolumna del dataset",color="orange",fontweight="bold",fontsize=14)

sns.kdeplot(data=tips, x="total_bill", hue="time", ax=axes[1,1], color="orange")

sns.kdeplot(data=tips, x="total_bill", hue="time", multiple="stack", ax=axes[1,2], color="orange")
axes[1,2].set_title("Apila las distribuciones\ncondicionales",color="orange",fontweight="bold",fontsize=14)

for n in range(0,2):
    for m in range(0,3):
        #Formato de los ejes
        axes[n,m].tick_params(axis='x', labelsize =12, colors="orange",grid_color='orange',length=6, width=2)
        axes[n,m].tick_params(axis='y', labelsize =12, colors="orange",grid_color='orange',length=6, width=2)
        #Seteo el grosor y color de los ejes:
        axes[n,m].spines['bottom'].set_linewidth(1.5)
        axes[n,m].spines['left'].set_linewidth(1.5)
        axes[n,m].spines['right'].set_linewidth(1.5)
        axes[n,m].spines['top'].set_linewidth(1.5)
        axes[n,m].spines['right'].set_color("orange")
        axes[n,m].spines['top'].set_color("orange")
        axes[n,m].spines['bottom'].set_color("orange")
        axes[n,m].spines['left'].set_color("orange")
        #Fondo del gráfico de color gris claro
        axes[n,m].patch.set_facecolor('xkcd:light grey')
        #Seteo la opacidad del fondo del grafico
        axes[n,m].patch.set_alpha(0.3)



#Fondo general de color gris oscuro
plt.figure(1).patch.set_facecolor('xkcd:dark grey')

#Fondo general de color gris oscuro
plt.figure(1).patch.set_facecolor('xkcd:dark grey')

#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()

plt.show()