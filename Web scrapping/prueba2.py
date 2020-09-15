import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://es.wikipedia.org/wiki/Grey%27s_Anatomy'
respuesta = requests.get(
    url,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
)

print(respuesta.status_code)

soup = BeautifulSoup(respuesta.content, 'html.parser')

table = soup.find('table', attrs={'class':'wikitable'})
# print(table)
# tabla_body= table.find("tbody")
table_rows = table.find_all('tr')

res = []
for tr in table_rows:
    td = tr.find_all('td')
    print(td)
    row = [str(i.text.strip().split("\n")) for i in td if str(i.text.strip().split("\n"))]
    if row:
        res.append(row)
# columns=["Year", "Mintage", "Quality", "Price"]

# print(res)

df = pd.DataFrame(res)
print(df)