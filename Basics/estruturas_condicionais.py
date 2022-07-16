
Valor_da_passagem = 4.30

valor_da_corrida = input("Qual é o valor da corrida? ")
valor_da_corrida = float(valor_da_corrida)

if valor_da_corrida <= Valor_da_passagem * 5:
    print("Pegue a corrida")
elif valor_da_corrida <= Valor_da_passagem * 6:
    print("Aguarde um momento o valor da corrida pode baixar")
else:
    print("Pegue o ônibus")