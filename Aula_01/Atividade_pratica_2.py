# Faça um programa que leia 3 números e informe o maior número e o menor.

num1 = float (input("Digite o primeiro número: "))
num2 = float (input("Digite o segundo número: "))
num3 = float (input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O primeiro número,", num1, ",é o maior de todos")

elif num2 > num1 and num2 > num3:
    print("O segundo número,", num2, ",é o maior de todos")

elif num3 > num1 and num3 > num2:
    print("O terceiro número,", num3, ",é o maior de todos")

elif num1 == num2 and num1 > num3:
    print("O primeiro e o segundo números,", num1, "e", num2, ",são os maiores")

elif num2 == num3 and num2 > num1:
    print("O segundo e o terceiro números,", num1, "e", num2, ",são os maiores")

elif num1 == num3 and num1 > num2:
    print("O primeiro e o terceiro números,", num1, "e", num3, ",são os maiores")

else:
    print("Condição inválida")

if num1 < num2 and num1 < num3:
    print("O primeiro número,", num1, ",é o menor de todos")

elif num2 < num1 and num2 < num3:
    print("O segundo número,", num2, ",é o menor de todos")

elif num3 < num1 and num3 < num2:
    print("O terceiro número,", num3, ",é o menor de todos")

elif num1 == num2 and num1 < num3:
    print("O primeiro e o segundo números,", num1, "e", num2, ",são os menores")

elif num2 == num3 and num2 < num1:
    print("O segundo e o terceiro números,", num1, "e", num2, ",são os menores")

elif num1 == num3 and num1 < num2:
    print("O primeiro e o terceiro números,", num1, "e", num3, ",são os menores")

else:
    print("Condição inválida")