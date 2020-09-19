import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import kdeplot
from seaborn import load_dataset

tips = load_dataset("tips")
tips.head()
#Creo una figura
plt.figure()
#Declaro el grafico que se insertará en esa figura
sns.kdeplot(data=tips, x="total_bill", hue="size")
plt.title("Distribuciones segun tamaño")

#Creo una figura
plt.figure()
#Declaro el grafico que se insertará en esa figura
sns.kdeplot(
   data=tips, x="total_bill", hue="size",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
plt.title("Cambiando la apareciendia\nde las distribuciones")

#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()
plt.figure(2).tight_layout()

plt.show()