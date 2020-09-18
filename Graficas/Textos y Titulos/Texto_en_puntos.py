import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

#Puedo cambiar el color y tamaño de la fuente
plt.xlabel('Smarts', fontsize=14, color='blue')
plt.ylabel('Probability', fontsize=14, color='red')
# plt.title('Histogram of IQ', fontsize=18, color='purple')
plt.title(r'$\sigma_i=15$', fontsize=18, color='purple')
#marco un punto en el grafico:
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

#https://matplotlib.org/tutorials/introductory/pyplot.html