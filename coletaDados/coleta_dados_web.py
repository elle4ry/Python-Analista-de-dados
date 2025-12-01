import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.content, 'html.parser')

#exibir o texto
# print(extracao.find_all())

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all('p'):
    titulo = linha_texto.text.strip()
    print('Titulo: ', titulo)

'''
Desafio
Filtrar tags ['h2', 'p']
Contar quantos h2 e p existem no documento (linha_texto.name == tag)
'''
# Conta a quantidade de h2 e p
contador_h2 = 0
contador_p = 0

for linha_texto in extracao.find_all(['h2','p']):
    if linha_texto.name == 'h2':
        contador_h2 += 1 # contar = contar + 1
    elif linha_texto.name == 'p':
        contador_p += 1

print('Contador texto: ', contador_p)
print('Contador subtitulo: ', contador_h2)

'''
Exibir somente o texto das tags h2 e p
'''
for linha_texto in extracao.find_all(['h2','p']):
    if linha_texto.name == 'h2':
        subtitulo = linha_texto.text.strip()
        print('SubTitulo: \n', subtitulo)
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('Paragrafo: \n', paragrafo)

'''
Exibir tags aninhada (tags dentro de tags)
'''
for titulo in extracao.find_all(['div','ul','li']):
    print('\n Titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings(['div','ul','li']):
        for a in link.find_all('a', href=True):
            print('Texto Link: ', a.text.strip(), ' | URL: ', a['href'])