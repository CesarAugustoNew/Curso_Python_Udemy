# Faça um programa que receba dois numeros inteiros e mostre qual deles e o maior

numero1: int = int(input('Digite o primeiro numero:'))
numero2: int = int(input('Digite o segundo numero:'))


if numero1 and numero2 < 0:
    print(f"o numero deve ser maior que zero ")
elif numero1 > numero2:
    print(f"{numero1} e maior que {numero2}")
elif numero1 < numero2:
    print(f"{numero2} e maior que {numero1}")
else:
    print("os numeros sao iguais")


#Faça um programa que leia um numero inteiro fornecido pelo usuario. Se esse numero for positivo, calcule a raiz quadrada do numero e apresente-a. Se o numero for negativo, mostre uma mensagem dizendo que o numero e invalido.

from math import sqrt

numero: int = int(input('Digite um numero:'))

if numero < 0:
    print(f"{numero} e invalido")
else:
    print(f"A raiz quadrada de {numero} e {sqrt(numero)}")


# Faca um programa que recebe um numero inteiro e informe se esse numero e par ou impar

numero: int = int(input('Digite um numero:'))

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} e impar")