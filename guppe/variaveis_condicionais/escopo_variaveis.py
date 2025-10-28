"""
Escopo de variaveis

Dois casos de escopo:

1- Variaveis globais;
    - Variaveis globais sao reconhecidas, ou seja, seu escopo compreende, todo o programa.

2- Variaveis locaos
    - Variaveis locais sao reconhecidas apenas no bloco onde foram declaradas ou seja seu escopo esta limitado ao bloco onde foi declarado

Para declarar variaveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variavel nos nao colocamos o tipo de dado dela.
Este tipo e inferido ao atribuirmos o valor a mesma.

Exemplo em C
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10 # A variavel novo esta declarada localmente dentro do bloco if. portanto e local
    print(novo)