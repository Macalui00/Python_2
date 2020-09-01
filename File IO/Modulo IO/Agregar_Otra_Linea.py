import io

#Agregar otra linea al fichero:
fichero = open('fichero.txt','a')  
fichero.write('\nOtra línea más abajo del todo')
fichero.close()
#La variante 'a+' permite crear el fichero si no existe:
#fichero = open('fichero_inventado.txt','a+')

# Para poder ver lo que agregamos:
fichero = open('fichero.txt','r') 
info = fichero.read()
print(info)
fichero.close()

"""Esta data tan interesante fue obtenida de: https://docs.hektorprofe.net/python/manejo-de-ficheros/ficheros-de-texto/"""