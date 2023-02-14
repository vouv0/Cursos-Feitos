#buscando data e hora em um site
import urllib3
from bs4 import BeautifulSoup


def faz_requisicao(site):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    manager = urllib3.PoolManager()
    return manager.request('GET', site, headers={'User-Agent': 'Mozilla/5.0'})


def le_site(site):
    response = faz_requisicao(site)
    return BeautifulSoup(response.data, 'html.parser')


bs = le_site('https://www.horariodebrasilia.org/')
tag_hora = bs.find('p', id='relogio')
tad_data = bs.find('h3', id='dia-topo')

print(tag_hora.text)
print(tad_data.text)
