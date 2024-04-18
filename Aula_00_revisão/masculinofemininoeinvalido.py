# exercicio 3 - Faça um Programa que imprima na tela "Feminino", "Masculino" ou "Sexo inválido" a partir de
# uma letra digitada: F ou f para feminino, M ou m para masculino e qualquer outra letra para sexo inválido.

sexo = input("Digite F para Feminino ou M para Masculino: ")

if sexo == "F" or sexo == "f":
    print("Feminino")

elif sexo == "M" or sexo == "m":
    print("Masculino")

else:
    print("Sexo Inválido")