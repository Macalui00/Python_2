import matplotlib.pyplot as plt
import numpy as np

y = [1,2,3,2,1,3,2,1,2,3,4,5,4,30,10,1]
plt.subplots(figsize = (10,10))
plt.subplot(2,2,1)
plt.pie(y)
plt.xlabel('mi grafico')
plt.title('titulo de mi grafico')
plt.legend( ('Etiqueta1',), loc = 'upper left')
plt.draw()
#savefig("mi-grafico1",dpi=300)
#close()
plt.grid(True)

n = 20
Z = np.ones(n)
Z[-1] *= 2

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.subplot(2,2,2)
plt.pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
plt.axis('equal')
plt.xticks(())
plt.yticks()

impr = ["b/n", "color", "dúplex", "A3"]
vol = [25, 31, 46, 10]
expl =(0, 0.05, 0, 0)
plt.subplot(2,2,3)
plt.pie(vol, explode=expl, labels=impr, autopct='%1.1f%%', shadow=True)
plt.title("Impresión", bbox={"facecolor":"0.8", "pad":5})
# plt.legend(loc = "upper right")

turistas = [86.9, 81.8, 75.9, 60.7, 58.2, 39.3, 37.7, 37.6, 37.5, 35.4]
paises = ['Francia', 'España', 'EEUU', 'China', 'Italia',
          'México', 'Reino Unido', 'Turquía', 'Alemania', 'Tailandia']

explode = [0, 0.2, 0, 0, 0, 0.4, 0, 0, 0, 0]  # Destacar algunos
plt.subplot(2,2,4)
plt.pie(turistas, labels=paises, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('TOP 10 DESTINOS TURÍSTICOS EN 2017')

# plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.subplots_adjust(left=0.125, #sirve para cambiar el espacio entre los subtramas.
                    bottom=0.125, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)

plt.show()

#https://python-para-impacientes.blogspot.com/2014/08/graficos-en-ipython.html
#https://www.hektorprofe.net/curso/visualizacion-graficos-matplotlib-python/tipos-de-graficos