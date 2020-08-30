import requests
import http

res = requests.get("https://news.ycombinator.com/")

print(res)
print(res.ok)
print(res.headers)
#Lo mas importante:
print(res.text)
#-----------------------------------------------
url = "http://www.google.com"
# url = "http://www.google.com/asckas/asdacs"
response = requests.get(url)

print(f"Tu request a {url} se retorno con el codigo de estado {response.status_code}")
#Retorna un codigo 300 que significa que funcionó
#Ahora si cambiamos el URL a algo que no existe...
#Ahora recibimos un codigo 404...
print(response.text)