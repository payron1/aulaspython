# Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

entrada = 0
pares = []
impares = []

for x in range (10):
    entrada = int (input ("Escreva um número inteiro: "))

    if int(entrada) %2 == 0:
        pares.append(int(entrada))

    elif int(entrada) %2 !=0:
        impares.append(int(entrada))

print ("Os números pares são ", pares)
print ("Os números impares são ", impares)