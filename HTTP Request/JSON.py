import requests

url = "https://icanhazdadjoke.com/"

# response = requests.get(url)
response = requests.get(url, headers={"Accept" : "text/plain"})
#Yo no quiero el contenido HTML sino la version de plain text

print(response.text)

#La mayoria de las paginas web no estan seteada para solo darte el texto plano de esta manera
#Ejemplo que pasa si uso google:
url2 = "https://www.google.com/"

response2 = requests.get(url, headers={"Accept" : "text/plain"})

print(response2.text)

#Entonce plain text esta bien pero hay otra manera que es mejor para lo que queremos que es JSON
#Entonces si cambio lo siguiente a application/json:
response = requests.get(url, headers={"Accept" : "application/json"})
#Esto lo que pide es por favor enviame la version Json de la página web

print(response.text)
print(response.json()) #este es el que realmente toma el json y lo convierte en python

#Parecen iguales pero si hago el type:
print(type(response.text)) #Entonces no puedo utilizar este porque es un string, porque no puedo pedirle dame el joke al string
print(type(response.json())) #Es un diccionario

#Entonces guardemos la respuesta json a una variable:
data = response.json()
#Entonces aca si puedo hacer cosas como:
print(data["joke"])
print(f"status: {data['status']}")