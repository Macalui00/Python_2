"""Selecciono el archivo, indico su ruta y la palabra que deseo buscar y me retorna un archivo txt con la cabecera, las lineas coincidentes, el numero de aparicion, etc."""

import csv
import os

def comprobarExtension(arch_csv):
    #Verifico si el archivo tiene extension
    if "\." not in arch_csv:
        print(arch_csv)
    else:
        #Si no tiene le inserto extension csv:
        print(arch_csv)
        arch_csv = arch_csv + ".csv"
        print(arch_csv)
    return arch_csv

def comprobarExistencia(nombre, direccion):
    #Reemplazo la las \ por /:
    direccion = direccion.replace("\\", "/")
    #Reviso si el archivo no existe:
    if not(os.path.exists(direccion + "/" + nombre)):
        print(f"No existe un archivo con el nombre {nombre} en la ruta actual")
        nombre = input("Ingrese el nombre del archivo: ")
        while not(os.path.exists(nombre)):
            print(f"No existe un archivo con el nombre {nombre} en la ruta actual")
            nombre = input("Ingrese el nombre del archivo: ")
    return nombre

arch_csv = input("Ingrese el nombre del archivo csv: ")    
arch_csv = comprobarExtension(arch_csv)
direccion = input("Ingrese direccion del archivo csv: ")
#Me ubico en la direccion actual    
os.chdir(direccion)
print("Dirección actual: %s" % os.getcwd())
#Reviso si existe el archivo
arch_csv = comprobarExistencia(arch_csv, direccion)
#Obtengo palabra clave:
palabra = input("Ingrese palabra clave que desea buscar en el archivo: ")
with open(arch_csv, 'r') as file:
    reader = csv.reader(file)
    linea = 0
    exitoso = 0
    for row in reader:
        if linea == 0:
            f = open ("Resultados.txt", "a")
            f.write(f"-----------------------------------------------------------------------------------------------------------------------------------------\r")
            f.write(str(row) + f"\n")
            f.write(f"-----------------------------------------------------------------------------------------------------------------------------------------\r")
            f.close()
            linea += 1
        else:
            for pal in row:
                print(type(palabra))
                if palabra in pal:
                    print(palabra)
                    print(pal)
                    f = open ("Resultados.txt", "a")
                    exitoso += 1
                    f.write(f"-----------------------------------------------------------------------------------------------------------------------------------------\n")
                    f.write(f"Número de línea de archivo original: {linea}\n")
                    f.write(f"Número búsqueda exitosa: {exitoso}\n")
                    f.write(f"-----------------------------------------------------------------------------------------------------------------------------------------\n")
                    f.write(str(row) + f"\n")
                    f.close()
            linea += 1
    f = open ("Resultados.txt", "a")
    f.write(f"-----------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write(f"Número total de líneas analizadas: {linea}\n")
    f.write(f"-----------------------------------------------------------------------------------------------------------------------------------------\n")
    f.close()