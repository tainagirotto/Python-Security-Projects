import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
region = dados['region']

print('Detalhes do IP externo: ')
print(f'IP: {ip}\nOrg: {org}\nRegião: {region}\nCity: {city}\nCountry: {country} ')