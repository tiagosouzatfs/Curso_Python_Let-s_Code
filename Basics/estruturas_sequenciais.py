
idade = input("Digite sua idade: ")
print(idade, type(idade))

idade = int(idade)
print(idade, type(idade))

print(type(float("123.12")))
print(type(str(123.12)))
print(bool('')) # se não tiver nada na string, é falso, qualquer outra coisa é verdadeiro
print(bool('abc'))
print(bool(0)) # se for 0 é falso, qualquer outra coisa é true
print(bool(124))
print(bool(-345))

salario_mensal = input("Digite o valor do seu salário mensal: ")
salario_mensal = float(salario_mensal)

gasto_mensal = float(input("Digite o valor do seu gasto mensal: "))

salario_anual = salario_mensal * 12
gasto_anual = gasto_mensal * 12

economizado_anual = salario_anual - gasto_anual

print("O valor economizado durante o ano é: ", economizado_anual)
