"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em Python são representados por chaves {}
"""

receita = {'jan': 100, 'feb': 200, 'mar': 300, 'apr': 400,}

print(receita)

# Interar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave: {chave}, Valor: {valor}')





