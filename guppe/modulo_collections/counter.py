"""
Modulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um interavel como parametro e cria um objeto do tipo Collections Counter que é parecido com um dicionario, contendo como chave o elemento da lista passado
como parâmetro e como a quantidade de ocorrências desses elemento
"""

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 3: 5, 2: 4, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3

texto = """Belém, também chamada de Belém do Pará, é um município brasileiro e a capital do estado do Pará. Localizada na Região Norte do Brasil, 
às margens da baía do Guajará e a cerca de 2 120 quilômetros de Brasília, sua população é de 1 303 403 habitantes, segundo o Censo 2022, sendo o município mais populoso 
do estado, o segundo da Região Norte e o décimo segundo do país. Com uma área total de 1 059,458 quilômetros quadrados, a cidade abrange quarenta e duas ilhas que 
representam 65% de seu território, e apresenta clima equatorial quente e úmido, sendo a capital mais chuvosa do Brasil. Classificada entre os municípios com melhor 
qualidade de vida da Região Norte, possui um Índice de Desenvolvimento Humano (IDH) de 0,746 (alto), ocupando a 22.ª posição entre as capitais brasileiras.)"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
















