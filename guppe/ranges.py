"""
Ranges

- Precisamos conhecer o loop for para usar o ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequencia numericas, não de forma aleatoria, mas sim de maneira especificada

Formas gerais:

#Forma 01

range(valor_de_parada)

OBS: valor_de_para não inclusive (inicio padrao 0, e passo de 1 em 1)

#Forma 01
for num in range(11):
    print(num, end=' ')

# Forma 02

range(valor_de_inicio, valor_de_para)

OBS: valor_de_parada nao inclusive (inicio especificado pelo usuario, e passo de 1 em 1)

for num in range(1, 11):
    print(num, end=' ')

# Forma 03

range (valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada nao inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario

# Forma 03
for num in range(5, 55, 2):
    print(num, end=' ')

# Forma 04 (Inversa)

range (valor_inicio, valor_de_parada, passo)
#OBS: valor_de_parada nao inclusive (valor_inicio especificado pelo usuario, e passo especificado pelo usuario

# Forma 04
for num in range(10, 0, -1):
    print(num, end=' ')
"""




