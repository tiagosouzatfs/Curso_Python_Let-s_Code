import requests as r

url = 'https://api.covid19api.com/dayone/country/brazil'

req = r.get(url)
print(req.status_code)

dados = req.json()
#print(dados[0])

final_data = []
for obs in dados:
    #como vamos trabalhar com arquivos csv, temos que criar uma lista de listas
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
#print(final_data)
final_data.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])
#print(final_data)

#Posições
CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)): #não começa em 0 pq a primeira linha é o cabeçalho com as colunas
    final_data[i][DATA] = final_data[i][DATA][:10] # eliminando a hora do timezone, deixando só a data
#print(final_data)

import datetime as dt

for i in range(1, len(final_data)): #não começa em 0 pq a primeira linha é o cabeçalho com as colunas
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

import csv
with open('Aplicações/brasil_covid19.csv', 'w') as file:
    escritor = csv.writer(file)
    escritor.writerows(final_data)

print(type(final_data[100][DATA]))

#gerando e salvando a imagem de gráfico com as informações da 
#API: https://api.covid19api.com/dayone/country/brazil, através da API: https://quickchart.io/chart

def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label':labels[i],
                'data':y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data': y
            }
        ]

def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }

def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_datasets(y, labels)
    options = set_title(title)
    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart

def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content

def save_image(path, content):
    with open(path, 'wb') as image: #wb é um modo de escrita em arquivo binário
        image.write(content)

from PIL import Image
from IPython.display import display

def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)

y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels = ["Confirmados", "Recuperados"]

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('grafico.png', chart_content)
display_image('grafico.png')
