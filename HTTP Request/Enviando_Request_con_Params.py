#QUE ES UN QUERY STRING? Una manera de pasar datos a un servidor como parte de un GET request.
#http://www.example.com/?key1=value1&key2=value2

#Las maneras de poder acceder a esos valores y hacer algo serian:
# import requests

# response = requests.get("http://www.example.com/?key1=value1&key2=value2")
#pero hay una manera aun mejor de hacer esto:

# response = requests.get(
#     "http://www.example.com/",
#     params= {
#         "key1" : "value1",
#         "key" : "value2"
#     }
# )

import requests

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept" : "application/json"},
    # params={"term":"cat", "limit":1} #buscará los chistes que contengan gato
    params={"term":"cat"}
    )

data = response.json()
# print(data["results"])
# #Dentro de data tengo una variable results que es un array de chiste. Donde cada elemento es un diccionario
# #Para obtener un solo chiste, podemos ponerle otro parametro al request que sea limit.
# resultado = data["results"][0]
# print(resultado["joke"])

#Ponele que quiero mostrar todos los chistes:
resultados = data["results"]
for resultado in resultados:
    print(resultado["joke"])