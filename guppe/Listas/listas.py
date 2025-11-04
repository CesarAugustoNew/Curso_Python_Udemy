"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a fiderença de serem DINAMICO e tambem de podermos colocar qualquer tipo de dados.

Linguagens C/JAVA: Arrays

    - Possuem tamanho e tipo de dado fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dados: Nao possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As Listas em Python são representadas por: []

"""

type ([])

lista1 = [1, 99, 4, 3, 63, 34, 86, 43, 23, 3, 1]
lista2 = list(range(11))

# Podemos facilmente checar se determinado valor esta contido na lista
num = 1
if num in lista1:
    print(f"Encontrei o numero {num}")
else:
    print(f"Nao encontrei o numero {num}")

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))

# Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nos so conseguimos adicionar 1 elemento por vez
"""
print(lista1)
lista1.append(100)
print(lista1)

lista1.append([9,3,1])  # Coloca a lista como elemento unico sublistas, Com append, nos conseguimos adicionar 1 elemento por vez
print(lista1)
if [9,3,1] in lista1:
    print(f"Encontrei a lista")
else:
    print(f"Nao encontrei a lista")

lista1.extend([123,34,12]) # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
lista2.insert(2, 'Novo valor')
print(lista2)

# Podemos facilmente juntar duas listas

lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista4 = lista2.copy()
print(lista4)

# Podemos contar quantos elementos temos em uma lista
print(len(lista4))

# Podemos remover facilmente o ultimo elemento de uma lista
print(lista4)
lista4.pop()
print(lista4)

# Podemos remover um elemento pelo indice
lista4.pop(2)
print(lista4)

# Podemos remover todos os elementos
print(lista2)
lista2.clear()
print(lista2)