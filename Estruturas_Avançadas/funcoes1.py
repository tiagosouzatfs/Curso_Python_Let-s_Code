
def hello():
    print('Olá, mundo!')

hello()

def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media(8, 9, 10)
print(resultado)

resultado2 = calcula_media(valor1=9, valor2=9, valor3=10)
print(resultado2)

#delimitador de fim de frase para não pular uma linha
print('Olá', end='')
print(', Tiago')

# já inicializando os valores
def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media()
print(resultado)

#função recursiva
def funcaoRecursiva(numero):
    if (numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)

print("Testando a função recursiva:")
funcaoRecursiva(10)