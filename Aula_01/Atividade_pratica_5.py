# Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.


condition = True

soma=0
numero=[]

while condition:
    num=int(input('Digite um numero ou zero para finalizar: '))

    if num != 0:
        soma += num
        numero.append(num)
    else:
        break

print('Soma: ', soma)
print('Menor Valor: ', min(numero))
print('Maior Valor: ', max(numero))