import requests
from bs4 import BeautifulSoup

# La función get_main_news retornará un diccionario con todas las urls y títulos de noticias encontrados en la sección principal.
def get_main_news():
    url = 'https://www.cmmedia.es/noticias/castilla-la-mancha/'

    respuesta = requests.get(
        url,
        #le pasaremos por cabecera un user agent válido para evitar problemas de compatibilidad por parte de la web.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
    )

    # Si queremos ver la respuesta que ha dado el servidor al hacer la petición lo podremos hacer con status_code, también lo podemos usar para parar la ejecución sino recibimos un estado válido como por ejemplo el 404 o 500.
    print(respuesta.status_code)

    # Para ver el contenido utilizaremos text, aquí se guarda todo el html de la página.
    print(respuesta.text)

    # Con header veremos las cabeceras que nos devuelve la página, esta puede contener cookies, información sobre que tipo de servidor están usando, el tipo de contenido (json, html, texto), etc.
    print(respuesta.headers)

    # Aquí podemos ver la cabecera de la petición, es decir, la que enviamos nosotros.
    print(respuesta.request.headers)

    # Para ver el método que hemos usado lo haremos con method, en nuestro caso get que también se ve en la llamada de la función.
    print(respuesta.request.method)

    #Una vez hecha la petición, vamos a extraer la información que nos interesa, para ello pasaremos todo el contenido de la respuesta a BeautifulSoup 

    contenido_web = BeautifulSoup(respuesta.text, 'lxml')

    # ahora vamos a proceder a extraer la url y el div con BeautifulSoup y de paso ver algunas de sus funciones.

    # Lo que estamos haciendo en estas líneas es buscar la etiqueta ul, que tenga la clase news-list, que es la lista que contiene todas las urls.
    noticias = contenido_web.find('ul', attrs={'class':'news-list'})
    # Con el resultado de esa búsqueda, utilizaremos findChildren para encontrar todos los divs que usen la clase que media-body que es la que contiene la url y el título, esto nos devolverá una lista con todos los resultados encontrados.
    articulos = noticias.findChildren('div', attrs={'class':'media-body'})

    # Para obtener las urls y el titulo:
    noticias = []

    for articulo in articulos:
        print('=================================')
        # buscaremos en la etiqueta h3 y utilizamos a.get('href') para extraer el link 
        print(articulo.find('h3').a.get('href'))
        # buscaremos en la etiqueta h3 y utilizamos get_text() para extraer el titulo
        print(articulo.find('h3').get_text())
        print('=================================')
        noticias.append({
            'url': articulo.find('h3').a.get('href'),
            'titulo': articulo.find('h3').get_text()
        })
    return noticias

def launch_request(url):
    try:
        respuesta = requests.get(
            url,
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
        )
        respuesta.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    # si no devuelve un estado válido lanzará una excepción que parará la ejecución.
    return respuesta

def get_all_info_by_new(noticia):
    
    print(f'Scrapping {noticia["titulo"]}')

    respuesta = launch_request(noticia["url"])

    contenido_web = BeautifulSoup(respuesta.text, 'lxml')

    articulo = contenido_web.find('article', attrs={'class':'post'})

    noticia['fecha'] = articulo.find('time').get_text()
    # noticia['articulo'] = articulo.find('div', attrs={'class':'', 'id':''}).get_text()
    parrafos = articulo.find('div', attrs={'class':'', 'id':''}).find_all("p")
    noticia['articulo'] = ''
    for parrafo in parrafos:
        noticia['articulo'] = noticia['articulo'] + parrafo.get_text()
    print(noticia)

    return noticia
if __name__ == '__main__':
    noticias = get_main_news()
    
    for noticia in noticias:
        noticia = get_all_info_by_new(noticia)
        print('=================================')
        print(noticia["titulo"])
        print(noticia["articulo"])
        print('=================================')

#https://cosasdedevs.com/posts/web-scraping-con-requests-y-beautifulsoup-en-python/