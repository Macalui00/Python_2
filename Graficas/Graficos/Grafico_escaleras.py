# Gráfico de escaleras
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.step(x, y)
plt.show()