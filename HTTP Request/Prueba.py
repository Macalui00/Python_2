import requests
from bs4 import BeautifulSoup
session = requests.session()

url = "http://www.chistes.com/BuscarChiste.asp"
parametro = {"palabra": "pez"}
# s = session.post(url, parametro)
# print('[*] Las cookies están configuradas a: ')
# print(s.cookies.get_dict())
# print('[*] Ingresando a página de perfil...')
s = session.get(url, params = parametro)
html = s.text
soup = BeautifulSoup(html, "lxml")
divs = soup.find_all('div', attrs={'class': 'chiste'})
# print(divs)

for div in divs:
    print(div.text)


# #Obtengo el contenido de la pagina web
# page = requests.get(url).text 
# soup = BeautifulSoup(page, "lxml")

# #Busco los chistes
# chistes = html.find_all('table', attrs={'class': 'chiste'})

# print(chistes)