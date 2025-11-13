"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a Teoria dos Conjuntos da Matematica.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matematica:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;

"""

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 3, 3, 1}) # Repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo sera ignorado sem gerar error e não fara parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('tem o 3')
else:
    print('nao tem o 3')

# Importante lembrar que, alem de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados. então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Listas: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionarios: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Usos interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes informam manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista Python, ja que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos.
# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado
print(s)

# Remover elementos em um conjunto
r = {1, 2, 3}
print(r)

# Forma 1

r.remove(3) # Não é indice Informamos o valor a ser removido.

print(r)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2

r.discard(22)
print(r)

# OBS: Se o valor não for encontrado, nenhum erro é gerado


# Copiando um conjunto para outro

# Forma 1 - Deep Copy
z = {1, 2, 3}

novo = z.copy()
print(novo)

novo.add(4)
print(novo)
print(z)

# Forma 2 - Shallow Copy

novo = r

novo.add(4)

print(novo)
print(r)

# Podemos remover todos os itens de um conjunto

z.clear()
print(z)

# Metodos Matematicos de Conjuntos

#Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python tambem estudam Java

# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)


















