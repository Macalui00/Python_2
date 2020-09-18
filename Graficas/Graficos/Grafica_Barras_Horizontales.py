import matplotlib.pyplot as plt
import numpy as np

fechas = ['19/08/2019', '20/08/2019', '21/08/2019', '22/08/2019', '23/08/2019']
primas = [79, 80, 79, 80, 82]
plt.subplot(1,2,1)
plt.barh(range(5), primas, edgecolor='black')
plt.yticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
#xlim: Obtiene o establece los límites x de los ejes actuales.
plt.xlim(min(primas)-1, max(primas)+1)
plt.grid(True)

paises = ("Alemania", "España", "Francia", "Portugal")
posicion_y = np.arange(len(paises))
unidades = (342, 321, 192, 402)
plt.subplot(1,2,2)
plt.barh(posicion_y, unidades, align = "center", edgecolor='black')
plt.yticks(posicion_y, paises)
plt.xlabel('Unidades vendidas')
plt.title("Ventas en Europa")
plt.grid(True)

plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.show()