"""Contenido original del archivo story.txt:
Esta es una gran historia donde un gran dragon se gana a la princesa.
Se enamoran y huyen juntos hacia el reino muy muy lejano."""

f = open("story.txt")
print(f)
dato = f.read()
print(dato)
f.close()

#Ejecutarlo en consola...

"""Ejemplos de diferentes fopen que podes utilizar:
Abrir fichero de lectura : f = open("fichero.txt")
Abrir fichero de lectura : f = open("fichero.txt", "r")
Abrir fichero de lectura en binario : f = open("fichero.txt", "rb")
Abrir fichero para escribir desde cero : f = open ("fichero.txt", "w")
Abrir fichero para añadir al final : f = open ("fichero.txt", "a")
etc.
"""

#Puedo leer solo una cierta cantidad de caracteres:
f = open("story.txt")
dato = f.read(10) #Obtengo 10 caracteres
print(dato)
f.close()

#Puedo leer solo una linea:
f = open("story.txt")
dato = f.readline()
print(dato)
f.close()

#Para escribir el fichero desde cero, borrando/sobreescribiendo su contenido si lo hubiera
f=open("Story.txt","w")
f.write("machacando\n")
f.close()
f=open("Story.txt")
f.read()
f.close()

#Para escribir sobre un fichero existente, añadiendo contenido al final
f = open ("Story.txt", "a")
f.write("tras tres tris\n")
f.close()
f=open("Story.txt")
f.read()
f.close()