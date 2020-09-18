# Guardar un gráfico como .png/.pdf
import matplotlib.pyplot as plt

lista1 = [11,2,3,15,8,13,21,34]
lista2 = [2,3,4,2,3,6,4,10]
lista3 = [9,15,9,15,9,15,9,15]

plt.plot(lista1, label = "Enero")
plt.plot(lista2, label = "Febrero")
plt.plot(lista3, label = "Marzo")
plt.legend(loc="upper left") 
plt.show()

# savefig("archivo.png")   # Guardar en formato .png
# savefig("archivo.pdf")   # Guardar en formato .pdf

#puedo guardarlo con fondo transparente
# savefig('demo.png', transparent=True)