# Estilos de Líneas (linestyle=):
# -, Línea Sólida
# --, Línea discontinua
# :, Línea punteada
# -., Línea punteada discontinua. y
# None, Ninguna línea

# Marcadores (marker=):
# +, Cruz
# ., Punto
# o,Círculo
# *, Estrellas
# p, Pentágonos
# s, cuadrados
# x, Tachados
# D, Diamantes
# h, Hexágonos y
# ^, Triángulos

# Colores (color=):
# b, blue
# g, green
# r, red
# c, cyan
# m, magenta
# y, yellow
# k, black
# w, white

#Ejemplos
import matplotlib.pyplot as plt

lista1 = [11,2,3,15,8,13,21,34]
lista2 = [2,3,4,2,3,6,4,10]
lista3 = [9,15,9,15,9,15,9,15]

plt.plot(lista1,marker="o",linestyle="--", color="m",label="Enero")
plt.plot(lista2,marker="p",linestyle=":", color="c",label="Febrero")
plt.plot(lista3,marker="D",linestyle="-.", color="g",label="Marzo")
plt.legend(loc="upper right")
plt.show()