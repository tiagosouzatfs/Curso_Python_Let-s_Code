
'''contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, "item limpo")
    else:  
        print(contador, "itens limpos")

print("Fim da repetição do bloco while")'''

'''contador = 0

while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, "item limpo")
        else:  
            print(contador, "itens limpos")
    else:
        break
        
print("Fim da repetição do bloco while")'''

'''texto = input("Digite sua senha: ")

while texto != "letsCode":
    texto = input("Senha inválida, tente novamente: ")

print("Acesso permitido") '''

contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue  
    print(contador, "itens limpos")
        
print("Fim da repetição do bloco while")