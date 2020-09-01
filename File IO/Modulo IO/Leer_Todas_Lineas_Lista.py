import io 

# Generar una LISTA CON TODAS LAS LINEAS DEL FICHERO:
fichero = open('fichero.txt','r')
texto_arch = fichero.readlines()
fichero.close()
print(texto_arch)

"""Esta data tan interesante fue obtenida de: https://docs.hektorprofe.net/python/manejo-de-ficheros/ficheros-de-texto/"""