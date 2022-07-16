
nomes_paises = ["Brasil", "Argentina", "China", "Canadá", "japão"]
print(nomes_paises)

print("Tamanho da lista: ", len(nomes_paises))

print("País: ", nomes_paises[4])
print("País: ", nomes_paises[-1])

nomes_paises[4] = "Colômbia"
print("País: ", nomes_paises[4])
print(nomes_paises)

print(nomes_paises[1:3])
print(nomes_paises[1:-1])
print(nomes_paises[2:])
print(nomes_paises[:3])
print(nomes_paises[:])

print(nomes_paises[::2])
print(nomes_paises[::-1])

print("Brasil" in nomes_paises)
print("Canadá" not in nomes_paises)

lista_capitais = []
lista_capitais.append("Brasília")
lista_capitais.append("Buenos Aires")
lista_capitais.append("Beijing")
lista_capitais.append("Bogotá")
print(lista_capitais)

lista_capitais.insert(2, "Paris")
print(lista_capitais)

lista_capitais.remove("Buenos Aires")
print(lista_capitais)

removido = lista_capitais.pop(2)
print(removido, lista_capitais)

#tupla a partir de lista
tupla_capitais = tuple(lista_capitais)
print(type(tupla_capitais))