# Suponha que você está gerenciando uma competição esportiva e tem
# uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido
# por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.

# 2.Ordene a lista medias em ordem decrescente.

# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.

# 4.Exiba na tela a classificação final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a mais baixa.


# Lista de tuplas representando os resultados das equipes
resultados = [
    ("Equipe A", [10, 8, 9]),
    ("Equipe B", [7, 6, 8]),
    ("Equipe C", [9, 9, 9]),
    ("Equipe D", [8, 7, 6])
]

# Calcula a média das pontuações de cada equipe e armazena em uma nova lista
medias = [(equipe, sum(pontuacoes) / len(pontuacoes)) for equipe, pontuacoes in resultados]

# Ordena a lista de médias em ordem decrescente
medias.sort(key=lambda x: x[1], reverse=True)

# Cria uma nova lista com tuplas contendo o nome da equipe e sua média de pontuações
classificacao = [(equipe, media) for equipe, media in medias]

# Exibe na tela a classificação final das equipes
print("Classificação final:")
for equipe, media in classificacao:
    print(f"{equipe}: {media}")