import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    for artigoExtracao in artigo.find_all('h3'):
        titulo = artigoExtracao.text.strip()
        livro['Título'] = titulo

    for artigoExtracaoExtra in artigo.find_all(class_='price_color'):
        preco = artigoExtracaoExtra.text.strip()
        livro['Preço'] = preco
    contar_livros += 1
    catalogo.append(livro)

print('Total livros:', contar_livros)
print(catalogo)