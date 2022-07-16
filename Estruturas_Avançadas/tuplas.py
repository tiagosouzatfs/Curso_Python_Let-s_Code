# tupla é imutável

tupla_paises = ("Brasil", "Argentina", "China", "Canadá", "Japão")
print(tupla_paises, type(tupla_paises))

tupla_paises = "Brasil", "Argentina", "China", "Canadá", "Japão"
print(tupla_paises, type(tupla_paises))

tupla_estado = "São Paulo",
print(tupla_estado, type(tupla_estado))

print(len(tupla_paises))

print(tupla_paises[0])

b, a, c, ca, j = tupla_paises
print(b, c, j)
print(*tupla_paises)
#retorna quantas vezes um elemento aparece, é igual para listas
print(tupla_paises.count("Japão"))
print(tupla_paises)

#lista a partir de tupla
lista_paises = list(tupla_paises)
print(type(lista_paises))