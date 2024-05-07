import requests
from bs4 import BeautifulSoup

# URL da página que você deseja obter o HTML
url = 'https://www.youtube.com/watch?v=mop6g-c5HEY&ab_channel=ClearCode'

# Fazendo a solicitação GET
response = requests.get(url)

# Verificando se a solicitação foi bem sucedida (código de status 200)
if response.status_code == 200:
    # Imprimindo o HTML da página
    # Parseando o HTML com o BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find('title').text)

else:
    # Se a solicitação falhou, imprima o código de status
    print('Erro ao obter a página:', response.status_code)