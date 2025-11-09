"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a fiderença de serem DINAMICO e tambem de podermos colocar qualquer tipo de dados.

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


#Para adicionar elementos em listas, utilizamos a função append

#OBS: Com append, nos so conseguimos adicionar 1 elemento por vez

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

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso) # Por padrao, o split separa os elementos da lista pelo espaco entra elas.

# Exemplo 2
curso = 'Programaçao,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Prograçao', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca cyfrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# U tilizando for

soma = ''
for elemento in lista6:
    print(elemento)
    soma = soma + elemento
print(soma)

# Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print (numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul']

print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul

# Fazer acesso aos elementos de forma indexada inversa
print(cores[-1])
print(cores[-2])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
listaRepeticao = []
listaRepeticao.append(42)
listaRepeticao.append(42)
listaRepeticao.append(33)
listaRepeticao.append(33)
listaRepeticao.append(42)

print(listaRepeticao)

# Encontrar o indice de um elemento na lista

numerosLista = [5, 6, 7, 8, 9, 10]

# Em qual indice esta o valor 6
print(numerosLista.index(6))

# Em qual indice da lista esta o valor 9
print(numerosLista.index(9))

# Retorna o indice do primeiro elemento encontrado
print(numerosLista.index(4))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numerosLista.index(5, 1)) # Buscando a partir do indice 1
print(numerosLista.index(5, 2)) # Buscando a partir do indice 2
print(numerosLista.index(5, 3)) # Buscando a partir do indice 3
#print(numerosLista.index(5, 4)) # Buscando a partir do indice 4
# OBS: Caso nao tenha este elemento na lista sera apresentado erro ValueError


# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com parametro 'fim'

print(lista[:2]) # começa em 0, pega ate o indice 2 - 1

print(lista[:4]) # começa em 0, pega ate o indice 4 - 1

print(lista[1:3]) # começa em 1, pega ate o indice 3 - 1

# Trabalhando com slice de lista com parametros 'passo'

print(lista[1::2]) # começa em 1, vai ate o final, de 2 em 2

print(lista[::2]) # começa em 0, vai ate o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

# Soma, Valor Máximo, Valor Mínimo, Tamanho

# Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # máximo valor
print(min(lista)) # mínimo valor
print(len(lista)) # tamanho da lista



# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))






















