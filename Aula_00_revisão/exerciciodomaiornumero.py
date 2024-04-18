n1=3
n2=2
n3=5

if n1 > n2 and n1 > n3:
    print ("n1 é o maior que todos")

elif n2 > n1 and n2 > n3:
    print ("n2 é o maior que todos")

elif n3 > n1 and n3 > n2:
    print ("n3 é o maior que todos")

elif n1 == n2 and n1 > n3:
    print ("n1 e n2 é o maior que todos")

elif n2 == n3 and n2 > n1:
    print ("n2 e n3 é o maior que todos")

elif n1 == n3 and n1 > n2:
    print ("n1 e n3 é o maior que todos")

else:
    print ("Todos os números são iguais")

