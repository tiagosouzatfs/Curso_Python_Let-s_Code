
nomes_cidades = ['são Paulo', 'Londres', 'Tóquio', 'Paris']
for cidade in nomes_cidades:
    print(cidade)

# mesmo exemplo acima, mas com tupla
nomes_cidades = 'são Paulo', 'Londres', 'Tóquio', 'Paris' # com ou sem parênteses
for cidade in nomes_cidades:
    print(cidade)

for posicao in range(len(nomes_cidades)):
    print(nomes_cidades[posicao])


# com dicionários
cidade = {
    'nome':'Natal',
    'estado':'Rio Grande do Norte',
    'populacao_milhoes':'12.2'
}
for chave_cidade in cidade:
    print(f'{chave_cidade}: {cidade[chave_cidade]}')

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))