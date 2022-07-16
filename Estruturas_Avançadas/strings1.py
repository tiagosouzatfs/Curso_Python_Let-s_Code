
empresa = "Google"
print(empresa, type(empresa))

empresa = 'Google'
print(empresa, type(empresa))

empresa = "Let's Code"
print(empresa)

#Delimitador contrabarra \ é usado quando nas aspas duplas ou simples tem mais de uma vez na string
frase = "O professo Pietro da Let's Code disse: \"Hoje a pizza é por minha conta\""
print(frase)

empresa = "Google"
print(empresa[0])
print(empresa[:3])

nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasíla"
nomes_cidades = nomes_cidades.split(", ")
print(nomes_cidades)

cabecalho = "                MENU PRINCIPAL                   "
print(cabecalho.strip())

nome_cidade = 'rIo DE jaNeirO'
print(nome_cidade.title()) #Primeira letra maiúscula das palavras
print(nome_cidade.capitalize()) #Primeira letra maiúscula da frase
print(nome_cidade.lower()) #tudo minúsculo
print(nome_cidade.upper()) #tudo maiúsculo

nome_cidade = input("Que cidade do Brasil é conhecida como cidade maravilhosa? ")
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'rio de janeiro':
    print('Tente novamente')
    nome_cidade = input("Que cidade do Brasil é conhecida como cidade maravilhosa? ")
print('Booaaa, deu certo, é isso mesmo, parabéns.')