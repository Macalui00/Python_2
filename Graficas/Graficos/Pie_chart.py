import matplotlib.pyplot as plt
import numpy as np

y = [1,2,3,2,1,3,2,1,2,3,4,5,4,30,10,1]
#obtengo el mapa de colores 
cmap = plt.get_cmap("YlOrBr")
#Y de ese mapa de colores genero una lista de colores del primero al tamaño de la lista de elementos "y" * 100 y tomo colores de esa gama de 10 en 10
outer_colors = cmap(np.arange(start=1, stop=len(y)*100, step=10)) 
plt.subplots(figsize = (10,10))
plt.subplot(2,2,1)
plt.pie(y, colors=outer_colors)
plt.title('Pie Chart', fontsize=18, color="yellow")
plt.legend( ('Etiqueta1',), loc = 'upper left')

plt.draw()
#savefig("mi-grafico1",dpi=300)
#close()
plt.grid(True)

n = 20
Z = np.ones(n)
Z[-1] *= 2

plt.axes([0.15, 0.15, 0.15, 0.15])
plt.subplot(2,2,2)
plt.pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
plt.axis('equal')
plt.title('Pie Chart V.2', fontsize=18, color="yellow", pad=1)
# plt.xticks(())
# plt.yticks()

impr = ["b/n", "color", "dúplex", "A3"]
vol = [25, 31, 46, 10]
expl =(0, 0.05, 0, 0)
plt.subplot(2,2,3)
plt.pie(vol, explode=expl, labels=impr, autopct='%1.1f%%', shadow=True)
# plt.title("Pie Chart V.3", bbox={"facecolor":"0.8", "pad":5}, fontsize=18, color="yellow")
plt.title("Pie Chart V.3",  fontsize=18, color="yellow")
# plt.legend(bbox_to_anchor=(1.4,1))
plt.legend(bbox_to_anchor=(0.97, 1), loc='upper left', borderaxespad=0.)
# plt.legend(loc = "upper right")

turistas = [86.9, 81.8, 75.9, 60.7, 58.2, 39.3, 37.7, 37.6, 37.5, 35.4]
paises = ['Francia', 'España', 'EEUU', 'China', 'Italia',
          'México', 'Reino Unido', 'Turquía', 'Alemania', 'Tailandia']

explode = [0, 0.2, 0, 0, 0, 0.4, 0, 0, 0, 0]  # Destacar algunos
plt.subplot(2,2,4)
plt.pie(turistas, labels=paises, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('TOP 10 DESTINOS TURÍSTICOS EN 2017',fontsize=18, color="yellow")

# plt.subplots_adjust(wspace=0.5, hspace=0.5)
# plt.subplots_adjust(left=0.10, #sirve para cambiar el espacio entre los subtramas.
#                     bottom=0.10, 
#                     right=0.9, 
#                     top=0.9, 
#                     wspace=0.10, 
#                     hspace=0.30)
#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()

#Fondo general de color gris oscuro
plt.figure(1).patch.set_facecolor('xkcd:dark gray')
plt.figure(1).patch.set_alpha(0.5)

plt.show()

#https://python-para-impacientes.blogspot.com/2014/08/graficos-en-ipython.html
#https://www.hektorprofe.net/curso/visualizacion-graficos-matplotlib-python/tipos-de-graficos
#https://blog.algorexhealth.com/2018/03/almost-10-pie-charts-in-10-python-libraries/
#https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html