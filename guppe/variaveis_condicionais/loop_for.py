"""
Loop for

Loopt -> Estrutura de repetição
For -> Uma dessas estruturas

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteraveis

Exemplos de iteraveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
-Range
    numero = range(1, 10)
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterrando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não e incluso na lista

1, 2, 3, 4, 5, 6, 7, 8, 9 o 10 não

for numero in range(1,10):
    print(numero)
    
for indice, letra in enumerate(nome):
    print(nome[indice])
    
for indice, letra in enumerate(nome):
    print(letra)
    
for _, letra in enumerate(nome):
    print(letra)
    
    OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
    
 
qtd = int(input('Quantas vezes esse loop deve rodar ?'))
soma = 0

for numero in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')
"""
qtd = int(input('Quantas vezes esse loop deve rodar ?'))
soma = 0

for numero in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'geek university'
for letra in nome:
    print(letra, end='')






