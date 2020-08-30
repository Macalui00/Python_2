import requests
from bs4 import BeautifulSoup
session = requests.session()

def verificarRespuesta(resp):
    """Verifico si la respuesta dada por el usuario es correcta"""
    while resp != "Ing" and resp != "Esp":
        resp = input("¿Seleccione idioma? Ing/Esp ")
    return resp

def verificarRespuesta2(resp):
    """Verifico si la respuesta dada por el usuario es correcta"""
    while resp != "S" and resp != "N":
        resp = input("¿Desea ver todos los chistes? S/N ")
    return resp

def verificarRespuesta3(resp, divs):
    """Verifico si la respuesta dada por el usuario es correcta"""
    while resp > len(divs):
        resp = int(input(f"No poseemos tantos chistes con esa busqueda. Nuestra cantidad actual es: {len(divs)}. Ingrese otra cantidad. "))
    return resp

def obtenerRespuesta():
    """Verifico el idioma"""
    resp = input("¿Seleccione idioma? Ing/Esp ")
    resp = verificarRespuesta(resp)
    return resp

def todosLosChistes():
    resp = input("¿Desea ver todos los chistes? S/N ")
    resp = verificarRespuesta2(resp)
    return resp

def obtenerCantChistes(divs):
    resp = int(input("Ingrese la cantidad de chistes que desea: "))
    resp = verificarRespuesta3(resp, divs)
    return resp

def mostrarTodosChistSoup(divs):
    i = 1
    for div in divs:
        print("------------------------------------------------------------------------------------------------------------")
        print(f"Chiste nro {i} : ")
        print("------------------------------------------------------------------------------------------------------------")   
        print(div.text)
        print("------------------------------------------------------------------------------------------------------------")
        i = i+1

def mostrarTodosChistJSON(resultados):
    i = 1
    for resultado in resultados:
        print("------------------------------------------------------------------------------------------------------------")
        print(f"Chiste nro {i} : ")
        print("------------------------------------------------------------------------------------------------------------")  
        print(resultado["joke"])
        print("------------------------------------------------------------------------------------------------------------")
        i = i+1

def mostrarNChistesSoup(divs):
    i = 1
    #El usuario selecciona la cantidad y se verifica que no supere a la cantidad que hay en la lista
    cant = obtenerCantChistes(divs)
    #Se muestran por pantalla la cantidad de chistes
    for a in range(0,cant):
        print("------------------------------------------------------------------------------------------------------------")
        print(f"Chiste nro {i} : ")
        print("------------------------------------------------------------------------------------------------------------")     
        print(divs[a].text)
        print("------------------------------------------------------------------------------------------------------------")
        i = i+1 
        
def mostrarNChistesJSON(resultados):
    i = 1
    #El usuario selecciona la cantidad y se verifica que no supere a la cantidad que hay en la lista
    cant = obtenerCantChistes(resultados)
    #Se muestran por pantalla la cantidad de chistes
    for a in range(0,cant):
        print("------------------------------------------------------------------------------------------------------------")
        print(f"Chiste nro {i} : ")
        print("------------------------------------------------------------------------------------------------------------")     
        print(resultados[a]["joke"])
        print("------------------------------------------------------------------------------------------------------------")
        i = i+1 


respuesta = obtenerRespuesta()
if respuesta == "Esp":
    url = "http://www.chistes.com/BuscarChiste.asp"
    # http://www.chistes.com/BuscarChiste.asp?palabra=pez
    chiste = str(input("Ingrese de que quiere el chiste: "))
    parametro = {"palabra": chiste}
    s = session.get(url, params = parametro)
    html = s.text
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all('div', attrs={'class': 'chiste'})

    #Verifico si se quieren todos los chistes
    resp = todosLosChistes()
    if resp == "S":
        #Usuario quiere ver todos los chistes
        mostrarTodosChistSoup(divs)
    else:
        #El usuario no quiere ver todos los chistes
        mostrarNChistesSoup(divs)

elif respuesta == "Ing":
    url = "https://icanhazdadjoke.com/search"
    chiste = input("Ingrese de que quiere el chiste: ") 
    response = requests.get(
        url,
        headers={"Accept" : "application/json"},
        # params={"term":"cat", "limit":1} #buscará los chistes que contengan gato
        params={"term":chiste}
        )
    data = response.json()
    resultados = data["results"]
    #Verifico si se quieren todos los chistes
    resp = todosLosChistes()
    if resp == "S":
        #Usuario quiere ver todos los chistes
        mostrarTodosChistJSON(resultados)
    else:
        #El usuario no quiere ver todos los chistes
        mostrarNChistesJSON(resultados)
