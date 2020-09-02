import os

#Renombrar un archivo
# os.rename("MacaMaca","MariaMoria")
# print(os.listdir("./"))


"""Esta información tan interesante ha sido obtenida de: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion7/archivos.html"""

#Propio desarrollo
def comprobarResp(resp, nombre):
    while resp != "S" and resp != "N":
        resp = input(f"Respuesta incorrecta. El nombre ingresado es el siguiente: {nombre} esta ok? S/N ")
    return resp

def comprobarNombreViejo(resp,viejo_nombre):
    while resp == "N":
        viejo_nombre = input("Ingrese el nombre de la carpeta que quiere cambiar: ")
        resp = input(f"El nombre ingresado es el siguiente: {viejo_nombre} esta ok?")
        resp = comprobarResp(resp, viejo_nombre)
    return viejo_nombre

def comprobarNombreNuevo(resp,nuevo_nombre):
    while resp == "N":
        nuevo_nombre = input("Ingrese el nombre de la carpeta que quiere cambiar: ")
        resp = input(f"El nombre ingresado es el siguiente: {nuevo_nombre} esta ok?")
        resp = comprobarResp(resp, nuevo_nombre)
    return nuevo_nombre

#Para revisar si existe el archivo
def comprobarExistencia(nombre):
    if not(os.path.exists(nombre)):
        print(f"No existe un archivo con el nombre {nombre} en la ruta actual")
        nombre = input("Ingrese el nombre de la carpeta que quiere cambiar: ")
        while not(os.path.exists(nombre)):
            print(f"No existe un archivo con el nombre {nombre} en la ruta actual")
            nombre = input("Ingrese el nombre de la carpeta que quiere cambiar: ")
    return nombre

viejo_nombre = input("Ingrese el nombre de la carpeta que quiere cambiar: ")
viejo_nombre = comprobarExistencia(viejo_nombre)
# resp = input(f"El nombre ingresado es el siguiente: {viejo_nombre} esta ok? S/N ")
# resp = comprobarResp(resp, viejo_nombre)
# viejo_nombre = comprobarNombreViejo(resp, viejo_nombre)

nuevo_nombre = input("Ingrese el nuevo nombre de la carpeta: ")
resp = input(f"El nombre ingresado es el siguiente: {nuevo_nombre} esta ok? S/N")
resp = comprobarResp(resp, nuevo_nombre)
viejo_nombre = comprobarNombreNuevo(resp, viejo_nombre)

os.rename(viejo_nombre,nuevo_nombre)
print(f"Los elementos en la direccion actual: {os.getcwd()} son los siguientes: ")
for file in os.listdir("./"):
    print(file)