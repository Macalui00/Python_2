import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), #xy ubicacion del punto marcado, xytext ubicacion del texto
             arrowprops=dict(facecolor='pink', shrink=0.05), #formato de la flecha que señala el punto
             fontsize=15, color='pink' #Color y tamaño del texto
             )

plt.ylim(-2, 2)
plt.show()

#https://matplotlib.org/tutorials/introductory/pyplot.html