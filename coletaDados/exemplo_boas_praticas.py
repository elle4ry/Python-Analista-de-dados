import requests
import pandas as pd

# URL da API
url = "https://api.exemplo.com/dados"

# Fazer a requisição GET para a URL da API
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Converter a resposta em JSON
    data = response.json()

    # Criar um DataFrame do Pandas a partir dos dados JSON
    df = pd.DataFrame(data)

    # Exibir as primeiras linhas do DataFrame
    print(df.head())
else:
    print("Falha na requisição:", response.status_code)