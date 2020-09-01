import os

# Eliminar un archivo
os.chdir("MariaMoria")
#Creo el archivo en la direccion actual y escribo en el.
#getcwd: obtener direccion
archivo = open(os.getcwd()+'/datos.txt', 'w')
archivo.write("Se Feliz!")
archivo.close()
#Obtengo la direccion donde se encuentra.
print(os.getcwd())
#Muestro la lista de elementos en la carpeta actual
print(os.listdir("./"))
#Elimino el archivo indicado
os.remove(os.getcwd()+"/datos.txt")
#Muestro la lista de elementos en la carpeta actual luego de remover el archivo
print(os.listdir("./"))


#Eliminar una carpeta
#Remuevo carpeta
os.rmdir("MariaMoria")
#Intento acceder a esa carpeta y...
# os.chdir("MariaMoria")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# OSError: [Errno 2] No such file or directory: 'Ana_Carolina'
# Lanza una excepción OSError cuando intenta acceder al directorio que previamente elimino y este no encuentra.

"""Esta información tan interesante ha sido obtenida de: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion7/archivos.html"""