# exercicio 2 - Faca um programa que peça um número ao usuario e mostre se o valor é positivo ou negativo.

num = int(input("Digite um número: "))

if num > 0:
    print ("O valor é positivo")

elif num < 0:
    print ("O valor é negativo")

else:
    print ("O valor é zero")