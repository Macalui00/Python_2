import io

# Tambien podemos modificar una linea de un fichero:
fichero = open('fichero2.txt','r+')
texto = fichero.readlines()
# Modificamos la línea que queramos a partir del índice
texto[2] = "Esta es la línea 3 modificada\n"
# Volvemos a ponter el puntero al inicio y reescribimos
fichero.seek(0)
#Escribir varias lineas a la vez:
fichero.writelines(texto)
fichero.close()
# Leemos el fichero de nuevo para comprobar esto:
with open("fichero2.txt", "r") as fichero:
    print(fichero.read())

"""Esta data tan interesante fue obtenida de: https://docs.hektorprofe.net/python/manejo-de-ficheros/ficheros-de-texto/"""