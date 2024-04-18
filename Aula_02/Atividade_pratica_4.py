# Crie uma tupla para representar as informações de três palestrantes,
# cada uma contendo o nome, o tema da palestra e a instituição
# à qual estão vinculados.
# Exiba na tela as informações do terceiro palestrante,
# incluindo nome, tema da palestra e instituição.

# Criando uma tupla com as informações dos palestrantes
palestrantes = (
    ("João Silva", "Inteligência Artificial na Medicina", "Universidade Federal"),
    ("Maria Santos", "Desenvolvimento Sustentável", "Instituto Ambiental"),
    ("Carlos Oliveira", "Energias Renováveis", "Empresa Energética")
)

# Exibindo as informações do terceiro palestrante
terceiro_palestrante = palestrantes[2]
print("Nome:", terceiro_palestrante[0])
print("Tema da Palestra:", terceiro_palestrante[1])
print("Instituição:", terceiro_palestrante[2])