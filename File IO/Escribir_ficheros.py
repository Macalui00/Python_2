#RECOMENDACIÓN: PROBAR LAS SIGUIENTES COSAS POR SEPARADO PARA MEJOR VISUALIZACIÓN.

#Para escribir el fichero desde cero, borrando/sobreescribiendo su contenido si lo hubiera
f=open("Story.txt","w")
f.write("machacando\n")
f.close()
f=open("Story.txt")
datos = f.read()
print(datos)
f.close()

#Para escribir sobre un fichero existente, añadiendo contenido al final
f = open ("Story.txt", "a")
f.write("tras tres tris\n")
f.close()
f=open("Story.txt")
datos = f.read()
print(datos)
f.close()

"""Link de donde es sacada esta información tan interesante: http://chuwiki.chuidiang.org/index.php?title=Leer_y_escribir_ficheros_en_python#:~:text=En%20python%20los%20ficheros%20se,f%20%3D%20open(%22fichero."""