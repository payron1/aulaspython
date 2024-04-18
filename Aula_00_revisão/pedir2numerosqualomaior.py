# exercicio 1 - Faça um Programa que peça dois números ao usuário e imprima o maior deles.

num1 = int (input("Primeiro número: "))
num2 = int (input("Segundo número: "))

if num1 > num2:
    print(num1)

elif num2 > num1:
    print(num2)

else:
    print("Os números são iguais")