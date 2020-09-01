"""
Moviéndose por el fichero
Con f.tell() podemos saber en qué posición estamos del fichero y con f.seek() podemos desplazarnos por él, para leer o escribir en una determinada posición.

f.seek(n) : Ir al byte n del fichero
f.seek(n,0) : Equivalente al anterior
f.seek(n,1) : Desplazarnos n bytes a partir de la posición actual del fichero
f.seek(n,2) : Situarnos n bytes antes del final de fichero.
El segundo parámetro en estos ejemplos es

Ninguno o 0 : la posición es relativa al principio del fichero
1 : la posición es relativa a la posición actual
2 : la posición es relativa al final del fichero y hacia atrás.
"""
#Abrimos el fichero:
f = open ("Story.txt")
#Nos situamos al final del fichero:
f.seek(0,2)
#Averiguamos la posición en la que estamos, que coincide con el número de bytes del fichero puesto que estamos al final del mismo:
tell = f.tell()
print(tell)
#Nos situamos en la posición 30 del fichero:
f.seek(30)
#Leemos hasta el final del fichero:
datos = f.read()
#Mostramos por pantalla lo que leimos:
print(datos)
#Cerramos el archivo
f.close()

"""Link de donde es sacada esta información tan interesante: http://chuwiki.chuidiang.org/index.php?title=Leer_y_escribir_ficheros_en_python#:~:text=En%20python%20los%20ficheros%20se,f%20%3D%20open(%22fichero."""