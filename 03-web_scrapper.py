from bs4 import BeautifulSoup

import requests

# objeto site recebe todo o conteudo da requisição http do site.
site = requests.get('https://climatempo.com.br/').content # content para pegar o conteúdo de todo site
# objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')
# transforma o html em string
print(soup.prettify())
# encontrar alguma parte do código
temperatura = soup.find("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")
print(temperatura.string)
# pegar o título ou dados específicos
print(soup.title.string)
print(soup.a) # ancora
print(soup.p.string)
