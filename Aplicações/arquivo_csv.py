import csv

#dependendo do formato do arquivo pode ser que precise adicionar a codificação
with open('Aplicações/Brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)

print('---------------------------------------------------')

#pegar os dados da coluna 'novos_casos > 1' sem o cabeçalho das colunas, pulando a primeira linha (cabeçalho)
with open('Aplicações/Brasil_covid.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    cabecalho = next(leitor) # pule do leitor a primeira linha e armazene em cabeçalho
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)

print('-------------------------------------------------------')

# também podemos ler o arquivo csv sem o import csv do python, só com as propriedes dos arquivos
with open('Aplicações/Brasil_covid.csv', 'r') as arquivo_csv:
    leitor = arquivo_csv.read()
    leitor = leitor.split('\n')
    for linha in leitor:
        linha = linha.split(',')
        print(linha)

print('-------------------------------------------------------')

with open('Aplicações/users.csv', 'w') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Tiago', 'Felipe', 'tiago@emial.com', 'Masculino'])
    escritor.writerow(['Larissa', 'Alves', 'larissa@email.com', 'Feminino'])

print('-------------------------------------------------------')

header = ['nome', 'sobrenome']
dados = []
op = input("Oque deseja fazer?\n1 - Cadastrar\n0 - Sair\n")
while op != "0":
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    dados.append([nome, sobrenome])
    op = input("Oque deseja fazer?\n1 - Cadastrar\n0 - Sair\n")

with open('Aplicações/cadastro.csv', 'w', newline='') as cadastro_usuario:
    escritor = csv.writer(cadastro_usuario)
    escritor.writerow(header)
    escritor.writerows(dados)

with open('Aplicações/cadastro.csv', 'r') as ler_usuario:
    csv_reader = csv.reader(ler_usuario, delimiter=',')
    for row in csv_reader:
        print(row)

#DictReader e DictWriter

#Podemos também trabalhar com dicionários, nos quais a primeira linha é lida como a chave 
# e as demais são os respectivos valores:

with open('Aplicações/email.csv', 'r') as emails:
    leitor = csv.DictReader(emails, delimiter=';') #a primeira linha é lida como um cabeçalho
    for linha in leitor:
        print(linha['Login email']) #podemos chamar um valor específico de cada linha pela chave no cabeçallho


with open('Aplicações/names.csv', 'w', newline='') as csvfile:
    chaves = ['first_name', 'last_name'] # definimos o cabeçalho
    writer = csv.DictWriter(csvfile, fieldnames=chaves) # especificamos o cabeçalho

    writer.writeheader() # escrevemos o cabeçalho
    writer.writerow({'first_name': 'Senhor', 'last_name': 'Batata'}) # escrevemos linhas com as chaves e valores
    writer.writerow({'first_name': 'Will', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Elon', 'last_name': 'Musk'})
