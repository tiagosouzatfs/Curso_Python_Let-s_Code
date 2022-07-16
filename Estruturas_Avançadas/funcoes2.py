
def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media(10, 8, 9)
print(resultado)

# essa função *args vai receber todos os parâmetros de entrada que eu digitar, qualquer que seja e depois
# o programador ajusta a operação dentro da função de acordo as variáveis de entrada declaradas, como abaixo
# args tem como tipo uma tupla
def calcula_media(*args):
    print(type(args))
    soma = sum(args)
    media = soma / len(args)
    return media

resultado = calcula_media(10, 8, 9)
print(resultado)

# qualquer coisa depois do *args, tem que ser explicitamente declarado

def calcula_media(*args, margem):
    soma = sum(args)
    media = soma / len(args)
    return media + margem

resultado = calcula_media(10, 8, 9, margem = 0.3)
print(resultado)


# args tem como tipo um dicionário que é mapeado em chave e valor
def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome='Tiago', sobrenome='Souza')