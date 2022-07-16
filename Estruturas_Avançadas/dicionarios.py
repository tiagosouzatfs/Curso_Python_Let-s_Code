
dados_cidade = {
    'nome':'São Paulo',
    'estado':'São Paulo',
    'area_km2':'1550',
    'população_milhões':'12.18'
}
print(type(dados_cidade))
print(dados_cidade)

#inserir chave e valor no fim, caso haja a chave, será alterado apenas o valor
dados_cidade['pais'] = 'Brasil'
print(dados_cidade)
dados_cidade['area_km2'] = '1500'
print(dados_cidade)
print(dados_cidade['nome'])

#usar uma cópia fazendo atribuição vai repetir a alteração, aí para não acontecer isso, temos que usar o método copy
dados_cidade2 = dados_cidade
dados_cidade2['nome'] = 'Santos'
print(dados_cidade2)
print(dados_cidade)

dados_cidade3 = dados_cidade.copy()
dados_cidade3['estado'] = 'Rio de Janeiro'
print(dados_cidade)
print(dados_cidade3)

#atualizar um dicionário com outro dicionário
novos_dados = {
    'população_milhões':'15',
    'fundação':'25/01/1554'
}
dados_cidade.update(novos_dados)
print(dados_cidade)

#se pesquisar uma chave ou valor que não tiver acessando a posição, vai dar erro, tem 
# que usar método get para retornar none e não dar erro
#print(dados_cidade['prefeito'])
print(dados_cidade.get('prefeito'))

#retorna a lista de chaves do dicionário
print(dados_cidade.keys())
#retorna a lista de valores do dicionário
print(dados_cidade.values())
#retorna uma lista de tuplas com (chave,valor) de um dicionário
print(dados_cidade.items())