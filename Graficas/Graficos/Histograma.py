#Otra forma de representar distribuciones de datos es mediante la utilización de histogramas.
from seaborn import distplot
import matplotlib.pyplot as plt
from seaborn import load_dataset

tips = load_dataset("tips")
tips.head()

plt.figure(figsize=(7,7))
distplot(tips.total_bill)
#Si no se desea que el histograma incluya también el diagrama de desinad se ha de indicar asignando el valor falso a la opción kde.

plt.figure(figsize=(7,7))
distplot(tips.total_bill, kde=False)
plt.title("Histograma sin diagrama de desinad")

#Alternativamente lo que puede eliminar es el histograma configurando la opción hist a falso
plt.figure(figsize=(7,7))
distplot(tips.total_bill, hist=False
plt.title("Diagrama sin histograma")

# Finalmente se puede hacer el gráfico vertical, para lo que se ha de propiedad vertical ha de ser verdadera
plt.figure(figsize=(7,7))
distplot(tips.total_bill, vertical=True)

#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()
plt.figure(2).tight_layout()

plt.show()