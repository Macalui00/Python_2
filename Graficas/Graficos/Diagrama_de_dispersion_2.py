import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import kdeplot
from seaborn import load_dataset

tips = load_dataset("tips")
tips.head()

# Fondo de pantalla negro:
# plt.style.use("dark_background")

# cambiar el color de la grilla y el del fondo del grafico:
# sns.set(rc={'axes.facecolor':'xkcd:dark grey', 'figure.facecolor':'xkcd:dark'})

# Cambia el formato de los ejes:
sns.set(style="ticks", context="talk")
sns.lmplot(x="total_bill", y="tip", col="smoker", data=tips)


#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()

plt.show()