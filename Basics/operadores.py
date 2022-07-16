
from numpy import real_if_close, true_divide


x = 50
y = 2

# Operações básicas
print(x+y)
print(x-y)
print(x*y)
print(x/y) # divisão inteira que tem casa decimal

print(x ** y) # exponenciação
print(x % y) # resto da divisão
print(x // y) # divisão inteira truncando a casa decimal

tem_cafe = True
tem_pao = False

print(not tem_cafe)
print(tem_cafe or tem_pao)
print(tem_cafe and tem_pao)

dolar = 5.13
real = 1

print(dolar > real)
print(dolar < real)
print(dolar == real)
print(dolar >= real)
print(dolar <= real)
print(dolar != real)
