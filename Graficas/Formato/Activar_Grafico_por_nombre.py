import matplotlib.pyplot as plt
import numpy as np

plt.figure('Regiones')
plt.figure('Dispersión')
elementosx = np.random.rand(10)   # Genera array 10 elementos eje x
elementosy = np.random.rand(10)   # Genera array 10 elementos eje y
plt.scatter(elementosx, elementosy)
plt.figure('Regiones')
plt.plot(elementosx,elementosy)

plt.show()