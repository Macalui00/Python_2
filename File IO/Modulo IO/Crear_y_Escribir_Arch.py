import io
#Importando io si podemos ejecutar el código sin tener que ejecutarlo por cmd.

texto = "Una línea con texto\nOtra línea con texto"

#Crear un archivo y escribirlo:
# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
fichero = open('fichero.txt','w')  

# Escribimos el texto
fichero.write(texto) 

# Cerramos el fichero
fichero.close() 

# Leer el contenido de un archivo:
# Para poder ver lo que escribio:
fichero = open('fichero.txt','r') 
info = fichero.read()
print(info)
fichero.close()

"""Esta data tan interesante fue obtenida de: https://docs.hektorprofe.net/python/manejo-de-ficheros/ficheros-de-texto/"""