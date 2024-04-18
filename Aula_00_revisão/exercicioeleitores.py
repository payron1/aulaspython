# usuário de 16 a 18 anos pode votar, mas não é obrigado (eleitor facultativo)
# usuário de 18 a 65 anos tem que votar (eleitor obrigatório)
# usuário acima de 65 anos pode votar, mas não é obrigado (eleitor facultativo)

usuario = int (input("Qual sua idade ?"))

if usuario >=18 and usuario <=65:
    print("Eleitor obrigatório")

elif usuario >=16 and usuario <18:
    print("Eleitor facultativo")

elif usuario < 16:
    print("Não pode votar")

elif usuario > 65:
    print("Eleitor facultativo")

else:
    print("Eleitor invalido")