import io

#Para posicionar el puntero justo al inicio de la segunda línea, podríamos ponerlo justo en la longitud de la primera:
fichero = open('fichero.txt','r')
#Nos posicionamos al principio del archivo
fichero.seek(0)
# Leemos la primera línea y situamos el puntero al principio de la segunda utilizando el len:
fichero.seek( len(fichero.readline()) )
# Leemos todo lo que queda del puntero hasta el final
data = fichero.read()
print(data)
fichero.close()

"""Esta data tan interesante fue obtenida de: https://docs.hektorprofe.net/python/manejo-de-ficheros/ficheros-de-texto/"""