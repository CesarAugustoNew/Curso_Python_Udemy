"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças basicas:

1- As tuplas são representadas por parenteses ()

2 - As tuplas são imutáveis: Isso significa que ao ser criar uma tupla ela não muda. TOda operção em uma tupla gera um nava tupla

"""

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 5,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênteses ( (4) -> Não é tupla  (4,) -> É tupla  4, -> É tupla)

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)
# OBS: Gera erro (ValueError) se colocarmos um numero diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis

# Soma, Valor Máximo, Valor Mínimo e Tamanho
# Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(len(tupla))
print(max(tupla))
print(min(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # Tuplas são imutáveis, mas podemos sobrescrever seus alores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)


# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)


# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'f')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro' )

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificando em qual Índice um elemento esta na tupla

    print(meses.index('Março'))

    # OBS: Caso o elemento não exista, será gerado ValueError.

# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])



















