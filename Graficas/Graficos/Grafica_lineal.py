import numpy as np
import pylab as pl

#Creo dos arrays de 10 elementos
x = np.arange(1, 11)
y = np.random.randint(10, size=10)

print(x, y)

#Creo una grafica lineal (plot) con un array como eje x y el otro como eje y
# pl.plot(x, y)
# #Lo muestro
# pl.show()

#Otra manera de hacer algo parecido pero esta vez con una sola lista de valores
lista1 = [11,2,3,15,8,13,21,34]   # Declara lista1 con 8 valores
pl.plot(lista1)   # Dibuja el gráfico
pl.title("Título")   # Establece el título del gráfico
pl.xlabel("abscisa")   # Establece el título del eje x
pl.ylabel("ordenada")   # Establece el título del eje y
pl.show()