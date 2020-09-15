import requests
from bs4 import BeautifulSoup

# La función get_main_news retornará un diccionario con todas las urls y títulos de noticias encontrados en la sección principal.
def get_main_news():
    url = 'https://www.cmmedia.es/noticias/castilla-la-mancha/yo-me-quedo-aqui-testimonios-de-apuesta-por-el-mundo-rural-en-cmm/'

    respuesta = requests.get(
        url,
        #le pasaremos por cabecera un user agent válido para evitar problemas de compatibilidad por parte de la web.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
    )

    contenido_web = BeautifulSoup(respuesta.text, 'lxml')
    articulo = contenido_web.find('article', attrs={'class':'post'})
    noticia = {"fecha": '', "articulo" : ""}
    noticia['fecha'] = articulo.find('time').get_text()
    parrafos = articulo.find('div', attrs={'class':'', 'id':''}).find_all("p")
    noticia['articulo'] = ''
    for parrafo in parrafos:
        noticia['articulo'] = noticia['articulo'] + parrafo.get_text()
    print(noticia)
