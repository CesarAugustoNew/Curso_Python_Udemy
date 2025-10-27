# Faça um programa que determine e mostre os cinco primeiros multiplos de 3, considerando numeros maiores que 0

contador: int = 0
indice: int = 1

while contador < 5:
    if indice % 3 == 0:
        print(f'O numero {indice} e multiplo de 3')
        contador = contador + 1
    indice = indice + 1


# Faça um programa que utilize o comando while para mostra na tela uma contagem regressiva, iniciando em 10 e terminando em 0. Mostre tambem uma mensagem "FIM" apos a contage,

numero: int = 10

while numero >= 0:
    print(numero)
    numero = numero - 1
print('FIM')


# Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo seu valor na tela ate que seu valor seja 1000000

numero: int = 0

while numero < 100000:                  # 1forma de fazer
    numero = numero + 1000
    print(numero)

for n in range(0, 100001, 1000):        # 2forma de fazer
    print(n)