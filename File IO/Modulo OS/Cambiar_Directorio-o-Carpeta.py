import os

# Cambiar directorio/carpeta
os.chdir("MacaMaca")
print(os.getcwd())
os.listdir("./")
os.chdir("../")
print(os.getcwd())


"""Esta información tan interesante ha sido obtenida de: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion7/archivos.html"""