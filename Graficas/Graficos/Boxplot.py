# Gráfico de caja y bigotes o boxplot
import numpy as np
import matplotlib.pyplot as plt

jap = np.random.uniform(166, 176, 100)
ale = np.random.uniform(175, 185, 100)
arg = np.random.uniform(170, 180, 100)


# Cambio los colores para que se vea bien en VSC con tema oscura
plt.boxplot([jap, ale, arg],
            notch=True, patch_artist=True,
            capprops=dict(color="green"),
            medianprops=dict(color="orange"),
            whiskerprops=dict(color="pink"))
plt.xticks([1, 2, 3], ['Japón', 'Alemania', 'Argentina'])
plt.ylabel('Estaturas (cm)')

plt.show()

#https://nataliaacevedo.com/tipos-de-graficos-en-python-con-matplotlib/