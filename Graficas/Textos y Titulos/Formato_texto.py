import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

# Con fontweight puedo poner el subtitulo en negrita
fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
ax.set_title('axes title')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

# Set both x- and y-axis limits to [0, 10] instead of default [0, 1]
ax.axis([0, 10, 0, 10])

#Formatear texto
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        #bbox me permite crear como si fuera una caja con el texto adentro.
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

#Escribir texto con formato especial r'', se le indica las coordenadas x=2 e y=6
ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'unicode: Institut für Festkörperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)

#Tercer parametro es el formato de la marca del grafico
ax.plot([2], [1], 'o')
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            #Formato de la flecha.
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()