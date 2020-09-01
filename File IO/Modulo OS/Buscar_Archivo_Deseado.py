import os
import fnmatch 

def comprobarResp(resp):
    while resp != "S" and resp != "N":
        resp = input("Respuesta incorrecta. ¿Conoce la extension del archivo? S/N ")
    return resp

def comprobarResp2(resp):
    while resp != "S" and resp != "N":
        resp = input("Respuesta incorrecta. ¿Sabe si existe un solo archivo con ese nombre? S/N ")
    return resp

def mostrarDirecciones(direcciones):
    print("Las direcciones posibles son las siguientes: ")
    for dir in direcciones:
        print(dir)

def buscarArchSinExt():
    archivo = input("Ingrese el nombre del archivo sin su extensión: ")
    archivo = archivo + '.*'
    direc_inicial = 'C:\\'
    lista_direcciones = [os.path.join(ruta, arch) for ruta, _, archivos in os.walk(direc_inicial)
                                            for arch in fnmatch.filter(archivos, archivo)]
    mostrarDirecciones(lista_direcciones)

def buscarUnSoloArch(archivo):
    direc_inicial = 'C:\\'
    direc_deseada = ''
    for ruta, _, archivos in os.walk(direc_inicial):
        if archivo in archivos:
            direc_deseada = os.path.join(ruta, archivo)
            break
    print(f"El archivo buscado se encuentra en la ruta: {direc_deseada}")

def buscarTodosLosArch(archivo):   
    direc_inicial = 'C:\\'
    lista_direcciones = [os.path.join(ruta, archivo) for ruta, _, archivos in os.walk(direc_inicial)
                                            if archivo in archivos]
    mostrarDirecciones(lista_direcciones)

def conoceExtensionArch():
    resp = input("¿Conoce la extension del archivo? S/N ")
    resp = comprobarResp(resp)
    return resp

def unSoloArchConEseNombre():
    resp = input("¿Sabe si existe un solo archivo con ese nombre? S/N ")
    resp = comprobarResp2(resp)
    return resp 

resp =  conoceExtensionArch()
if resp == "S":
    archivo = input("Ingrese el nombre del archivo con su extensión: ")
    resp = unSoloArchConEseNombre()
    if resp == "S":
        buscarUnSoloArch(archivo)
    else:
        buscarTodosLosArch(archivo)
else:
    buscarArchSinExt()

