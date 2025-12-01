import requests

def enviar_arquivos():
    # caminho para o arquivo
    caminho = 'C:/Users/ellea/Downloads/produtos_informatica.xlsx'

    # enviar o arquivo
    requisicao = requests.post(url='https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})

    saida_requisicao = requisicao.json()
    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print('Arquivo enviado. Link para acesso', url)

def enviar_arquivo_chave():
    # caminho do arquivo e chave para upload
    caminho = 'C:/Users/ellea/Downloads/produtos_informatica.xlsx'
    chave_acesso = 'precifo fazer o login para ter' # api key

    #enviar o arquivo
    requisicao = requests.post(
        url='https://upload.gofile.io/uploadFile',
        files={'file':open(caminho,'rb')},
        headers={'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print('Arquivo enviado com chave. Link para acesso', url)

def receber_arquivo(file_url):
    # recebe arquivo
    requisicao = requests.get(file_url)

    # salva o arquivo
    if requisicao.ok:
        with open('arquivo_chave.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso')
    else:
        print('Erro ao baixar arquivo:', requisicao.json())

#enviar_arquivos()
receber_arquivo('https://gofile.io/d/PfCzNW')