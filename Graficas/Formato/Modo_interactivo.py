import pylab as pl

#Activar y desactivar el modo interactivo de dibujo
# se utilizan los métodos ion() y ioff() que activan o desactivan el modo interactivo de dibujo para añadir, o no, nuevos datos sobre el gráfico actual.

lista1 = [11,2,3,15,8,13,21,34]   # Declara lista1 con 8 valores
pl.plot(lista1)   # Dibuja el gráfico
pl.xlabel("abscisa")   # Inserta el título del eje X
pl.ylabel("ordenada")   # Inserta el título del eje Y
pl.ioff()   # Desactiva modo interactivo de dibujo


lista2 = [2,3,4,2,3,6,4,10]   # Declara lista2 con 8 valores
pl.plot(lista2)   # No dibuja datos de lista2
pl.ion()   # Activa modo interactivo de dibujo
pl.plot(lista2)   # Dibuja datos de lista2 sin borrar datos de lista1

pl.show()

#Para conocer en un momento dado qué modo está activo:
pl.isinteractive()   # La función devolverá True o False

#Los métodos show() o draw() fuerzan que la información se muestre en el gráfico (datos, títulos, etiquetas, etc.) aunque el modo interactivo esté desactivado
pl.ioff()   # Desactiva modo interactivo
lista3 = [9,15,9,15,9,15,9,15]   # Declara lista3 con 8 valores
pl.plot(lista3)   # No dibuja datos de lista3
pl.show()   # Fuerza dibujo de datos de lista3
pl.title("Gráfica")   # Establece nuevo título pero no muestra en gráfico
pl.show()   # Actualiza gráfico con nuevo título
pl.grid(True)  # Activa cuadrícula del gráfico pero no se muestra
pl.show()   # Muestra cuadrícula del gráfico
pl.ion()   # Activa modo interactivo de dibujo
