"""
Loop while

Forma geral

while expressão_booleana:
    //execução da loop

O bloco do while sera repetido enquanto a expressão booleaa for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso

Exemplo:

num = 5
num < 5

"""
# Exemplo 01
# OBS: Em um loop while, é importante que cuidemos do criterio de parada não causar um loop infinito
numero = 1

while numero < 10:
    print(numero)
    numero = numero +1

# Exemplo 02

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
