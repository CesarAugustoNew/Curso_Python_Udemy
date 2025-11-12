"""
Dicionarios

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;
"""

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])

#print(paises['ru'])
# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('ru'))
# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos None

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionario, como chaves de dicionarios

# Tuplas por exemplo são bastante interessantes de semre utilizadas como chave de dicionarios, pois as mesmas são imutaveis

localidade = {
    (35.6894, 39.6914): 'Escritorio em Tókio',
    (40.1245, 61.9939): 'Escritorio em Nova York',
    (18.2928, 144.4224): 'Escritorio em São Paulo',
}

print(localidade)
print(type(localidade))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 200, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 700})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario e a mesma.
# CONCLUSÃO 2: Em dicionarios, não podemos ter chaves repetidas.


# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 200, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos sempre informar a chave e caso nao encontre o elemento, um KeyError é retornadi
# OBS 2: Ao removermos um objeto, o valor deste objeto e sempre retornado

# Forma 2

del receita['fev']

print(receita)

# Se a chave não existir sera gerado um KeyError
# OBS: Neste caso o valor removido nao e retornado

# Imagine que voce tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos
"""
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
"""

# 1 - Poderiamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2500.00]
produto2 = ['God of War 4', 1, 200.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# 2 - Poderiamos utilizar uma Tupla para isso? Sim

produto1 = ['Playstation 4', 1, 2500.00]
produto2 = ['God of War 4', 1, 200.00]

carrinho = (produto1, produto2)

print(carrinho)

# 3 - Poderiamos utilizar um Dicionario para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2500.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 156.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre cade informação.
























