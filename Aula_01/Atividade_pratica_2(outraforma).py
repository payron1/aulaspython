# Faça um programa que leia 3 números e informe o maior número e o menor.
num1 = float (input("Digite o primeiro número: "))
num2 = float (input("Digite o segundo número: "))
num3 = float (input("Digite o terceiro número: "))

lista = [num1, num2, num3]

maior = max(lista)
menor = min(lista)

print("O maior é ", maior)
print("O menor é ", menor)