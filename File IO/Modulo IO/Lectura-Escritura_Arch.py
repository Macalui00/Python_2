import io

# Lectura y escritura de un fichero a la vez:
# Para lo cual, creamos un fichero de prueba con 4 líneas
fichero = open('fichero2.txt','w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero.write(texto)
fichero.close()
# Lo abrimos en lectura con escritura y escribimos algo:
fichero = open('fichero2.txt','r+')
# Basicamente reescribe la primera linea del archivo:
fichero.write("0123456")
# Volvemos a poner el puntero al inicio y leemos hasta el final
fichero.seek(0)
data = fichero.read()
print(data)
fichero.close()

"""Esta data tan interesante fue obtenida de: https://docs.hektorprofe.net/python/manejo-de-ficheros/ficheros-de-texto/"""