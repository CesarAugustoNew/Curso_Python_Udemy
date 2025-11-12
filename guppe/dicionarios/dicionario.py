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
























