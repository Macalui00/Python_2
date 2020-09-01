"""Sintaxis general:
with EXPRESIÓN as VARIABLE:
    BLOQUE DE INSTRUCCIONES
    
Para el caso de los ficheros:
with open("FICHERO") as fichero:
    BLOQUE DE INSTRUCCIONES

Argumentos más importantes de funcion open:
with open("FICHERO", mode="MODO", encoding="CODIFICACIÓN") as fichero:
    BLOQUE DE INSTRUCCIONES

donde:
    "FICHERO" es la ruta absoluta o relativa hasta el fichero.
    "MODO" indica si el fichero se abre para leer, escribir o ambas cosas y si se trata de un fichero de texto o binario. El modo predeterminado es lectura en modo texto.
    "CODIFICACIÓN" indica el juego de caracteres del fichero: "utf-8" (UTF-8), "cp1252" (ASCII para Europa occidental), etc.
"""

#Ejemplos:
#Escitura:
ruta = "prueba.txt"
with open(ruta, mode="w", encoding="utf-8") as fichero:
    print("Hola", file=fichero)
    fichero.write("Hola\n")    

#Modo x: crea un fichero, si se ejecuta por segunda vez lo siguiente o si el fichero ya existe, se genera un error.
# ruta = "prueba.txt"
# with open(ruta, mode="x", encoding="utf-8") as fichero:
#     print("Hola", file=fichero)
#     fichero.write("Hola\n")

#Modo a: agregando la linea al final del fichero o, si no existe el fichero, lo crea.
ruta = "prueba.txt"
with open(ruta, mode="a", encoding="utf-8") as fichero:
    print("Hola", file=fichero)
    fichero.write("Hola\n")

"""Esta info tan interesante fue obtenida de: https://www.mclibre.org/consultar/python/lecciones/python-ficheros.html#with-as"""

    