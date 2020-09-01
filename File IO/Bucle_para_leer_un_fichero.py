#Abre un fichero y lo copia en otro

if __name__ == "__main__":
    f = open("origen.txt")
    g = open("destino.txt","w")
    #El siguiente bucle es una forma de recorrer un fichero de texto, obteniendo una línea cada vez.
    for linea in f:
        g.write(linea)
    g.close()
    f.close()

#El fichero se puede leer con f.readLine() que nos da una línea a la vez, PERO, incluyendo el retorno de carro "\n" al final. Cuando lleguemos a final de fichero nos devolverá una linea vacía.
#Una línea en blanco en medio del fichero nos sería devuelta como un "\n", no como una línea vacía "".

#El siguiente ejemplo hace la copia del fichero leyendo con readline() en un bucle hasta fin de fichero:
if __name__ == "__main__":
   f = open("origen.txt")
   g = open("destino.txt","w")
   linea = f.readline()
   while linea != "":
      g.write(linea)
      linea = f.readline()
   g.close()
   f.close()

"""Link de donde es sacada esta información tan interesante: http://chuwiki.chuidiang.org/index.php?title=Leer_y_escribir_ficheros_en_python#:~:text=En%20python%20los%20ficheros%20se,f%20%3D%20open(%22fichero."""