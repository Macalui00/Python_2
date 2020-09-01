import os

filename = "Mostrar_Directorio_Actual.py"
folder = "MODULO OS"

# Mostrar el tamaño del archivo en bytes del archivo pasado en parámetro:
tamano = os.path.getsize(os.path.join(filename))
print(tamano)

# Si estuviera en otra carpeta:
# tamano = os.path.getsize(os.path.join(folder, filename))

#Si quiero saber el tamaño de una carpeta
tamano = os.path.getsize("MacaMaca")
print(tamano)

"""Esta información tan interesante ha sido obtenida de: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion7/archivos.html"""