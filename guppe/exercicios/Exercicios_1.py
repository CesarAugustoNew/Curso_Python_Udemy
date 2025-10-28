#Faça um programa que leia um numero inteiro e imprima-o

numero: int = int(input("Digite um numero inteiro"))

#Faça um programa que peça para o usuário digitar três valor inteiros e imprima a soma deles.

numero1: int = int(input("Informe o primeiro inteiro"))
numero2: int = int(input("Informe o segundo inteiro"))
numero3: int = int(input("Informe o terceiro inteiro"))

soma: int = numero1 + numero2 + numero3
print(soma)

#Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos

valor1 = input ("Digite um numero valor")
valor2 = input ("Digite um numero valor")
valor3 = input ("Digite um numero valor")

soma: int = (valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)

print(f"A soma dos quadrados dos valor {valor1} com {valor2} e {valor3} e {soma}")