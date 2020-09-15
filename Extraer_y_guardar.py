import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

import xlwt

# wb = xlwt.Workbook()
# ws = wb.add_sheet('a test sheet')

#Indico la ruta
url_page = 'https://es.wikipedia.org/wiki/The_Umbrella_Academy_(serie_de_televisi%C3%B3n)'

#Obtengo el contenido de la pagina web
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")

#Busco aquella/s tabla/s que presente los atributos indicados
# tablas = soup.find_all('table', attrs={'class': 'wikitable plainrowheaders wikiepisodetable'})
tablas = soup.find('table', attrs={'class': 'wikitable plainrowheaders wikiepisodetable'})

#Leo el contenido de cada celda:

# for tabla in tablas:
#     tbody = tabla.find("tbody")
#     for fila in tabla.find_all("tr"):
#         celdas = fila.find_all('th')
#         if celdas == []:
#             for celda in fila.find_all('td'):
#                 name=celda.text
#                 print(name)
#         else:
#             for celda in celdas:
#                 name=celda.text
#                 print(name)

#Imprimo por pantalla la tabla de una manera mas linda:
contFila = ""
esp = " | "
for tabla in tablas:
    tbody = tabla.find("tbody")
    # x = 0
    # ws = wb.add_sheet(f'a test sheet {x}')
    for fila in tabla.find_all("tr"):
        for celda in fila.find_all('td'):
            # y = 0
            cont = celda.text
            # print(cont)
            contFila = contFila + esp + cont
            # cont = cont.encode('utf-8')
            # cont = cont.strip()
            # ws.write(x, y, cont)
            y = y + 1
        print(contFila)
        # x = x + 1
        contFila =""
        

# wb.save('BlastResults.xls')


    