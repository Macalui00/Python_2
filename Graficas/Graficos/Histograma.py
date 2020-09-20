#Otra forma de representar distribuciones de datos es mediante la utilización de histogramas.
from seaborn import distplot
import matplotlib.pyplot as plt
from seaborn import load_dataset
import seaborn as sns

tips = load_dataset("tips")
tips.head()

#Establezco la division de la figura
fig, axes = plt.subplots(2, 2, figsize=(10,6))
fig.suptitle('Diagrama de densidad',fontweight="bold",fontsize=18)

sns.set(style="whitegrid", font_scale=1.5)
sns.set(style='dark')

#Grafica 1
distplot(tips.total_bill, color="green",ax=axes[0,0])
#Si no se desea que el histograma incluya también el diagrama de desinad se ha de indicar asignando el valor falso a la opción kde.

#Grafica 2
distplot(tips.total_bill, kde=False, color="red",ax=axes[0,1])
plt.title("Histograma sin diagrama de desinad")

#Grafica 3
#Alternativamente lo que puede eliminar es el histograma configurando la opción hist a falso
distplot(tips.total_bill, hist=False, color="purple", ax=axes[1,0])
plt.title("Diagrama sin histograma")
"""FutureWarning: `distplot` is a deprecated ftplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a fh similar flexibility) oigure-level function with similar flexibility) or `histplot` (an axes-level function for histograms)."""

#Grafica 4
# Finalmente se puede hacer el gráfico vertical, para lo que se ha de propiedad vertical ha de ser verdadera
distplot(tips.total_bill, vertical=True, color="pink", ax=axes[1,1])

#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()

plt.show()