# operações com arquivo, leitura (r) e escrita (w)

#abrindo o arquivo e lendo diretamente
arquivo = open('/home/tiago/Lets_Code/Curso_Python/Apĺicações/dom_casmurro_cap_1.txt', 'r')
texto = arquivo.read()
print(texto)
arquivo.close()

# abrindo o arqivo e lendo linha por linha
arquivo = open('/home/tiago/Lets_Code/Curso_Python/Apĺicações/dom_casmurro_cap_1.txt', 'r')
linha = arquivo.readline()
while linha != '':
    print(linha, end="")
    linha = arquivo.readline() #todas às vezes que a função readline() for chamada ela itera uma linha
                               # no arquivo, é por isso que esse código e o de cima dão o mesmo resultado
arquivo.close()

# abrindo o arquivo e lendo com o for. Naturalmente, o for já itera linha por linha não precisa de função
arquivo = open('/home/tiago/Lets_Code/Curso_Python/Apĺicações/dom_casmurro_cap_1.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

# uma forma de abrir o arquivo e fechar automaticamente é usando a função "with"
with open('/home/tiago/Lets_Code/Curso_Python/Apĺicações/dom_casmurro_cap_1.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto)

#Escrita. Se o arquivo não estiver criado, a função write já cria
with open ('/home/tiago/Lets_Code/Curso_Python/Apĺicações/arquivo_teste.txt', 'w') as arquivo:
    arquivo.write('Primeira linha escrita com python\n')
    arquivo.write('Segunda linha escrita com python\n')
    arquivo.write('Terceira linha escrita com python\n')

with open ('/home/tiago/Lets_Code/Curso_Python/Apĺicações/arquivo_teste.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto, end='')

# pelo que eu entendi a operação de arquivo (a) é para atualizar o arquivo
with open ('/home/tiago/Lets_Code/Curso_Python/Apĺicações/arquivo_teste.txt', 'a') as arquivo:
    arquivo.write('Quarta linha escrita com python\n')

with open ('/home/tiago/Lets_Code/Curso_Python/Apĺicações/arquivo_teste.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto, end='')