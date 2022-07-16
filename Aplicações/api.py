#Utilição de API's públicas
#Tem que instalar pelo pip o requests: pip install requests

import requests

url =  'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)

#verificar o código de resposta http para ver se a API está disponível
print(req.status_code)

dados = req.json()

print(dados)


valor_reais = float(input('Informe o valor em R$ a ser convertido em dolar:\n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dolar valem US$ {(valor_reais / cotacao):.2f}')
