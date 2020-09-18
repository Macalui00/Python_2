# El método cla() borra toda la información relacionada con los ejes de un gráfico y el método clf() borra todo el gráfico. Por otro lado, close() termina el gráfico cerrando su ventana.
import matplotlib.pyplot as plt
import numpy as np

plt.cla()   # Borrar información de los ejes
plt.clf()   # Borrar un gráfico completo
plt.close()   # Terminar un gráfico