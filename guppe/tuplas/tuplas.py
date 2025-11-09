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

