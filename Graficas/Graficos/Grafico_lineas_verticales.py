import matplotlib.pyplot as plt
import numpy as np

sample_data = np.random.normal(0, 0.1, 1000)
x = np.arange(1, 11)
y = np.random.randint(10, size=10)

#caso stem
plt.subplot(2,2,1)
plt.stem(x, y)
plt.title("Stem")

#caso histograma
plt.subplot(2,2,2)
plt.hist(sample_data, rwidth=0.9) #Separacion entre barras rwidth
plt.title("Histograma")

#Definimos una lista con paises como string
paises = ['Estados Unidos', 'España', 'Mexico', 'Rusia', 'Japon']
#Definimos una lista con ventas como entero
ventas = [25, 32, 34, 20, 25]
 
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.subplot(2,2,(3,4))
plt.bar(paises, ventas)
plt.title("Cantidad de ventas por pais")
plt.xlabel("Pais")
plt.ylabel("Ventas")
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.savefig('barras_simple.png')
plt.show()