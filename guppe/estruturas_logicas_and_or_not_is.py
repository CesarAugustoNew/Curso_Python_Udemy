"""
Estruturas Logicas: and, or, not, is

Operadores unarios:
    - not
Operadores binarios:
    - and, or, is

Regras do funcinamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo.
"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuario!')
else:
    print('Voce precisa ativar sua conta. Por favor, cheque seu e-mail')