# Gerenciamento de Compras de Produtos

# Você foi contratado para desenvolver um programa simples para auxiliar
# em um processo de compra de produtos. O programa deve permitir ao
# usuário inserir o nome e o preço de vários produtos, perguntando
# se deseja continuar inserindo mais produtos após cada entrada.
# Ao final, o programa deve fornecer um resumo da compra, incluindo:
# A) O total gasto na compra.
# B) A quantidade de produtos que custam mais de R$1000.
# C) O nome do produto mais barato.

#Desenvolva o programa em Python utilizando conceitos de
#entrada/saída de dados, condicionais e laços de repetição.

barato = ''
total = maior_que_mil = cont = menor = 0
resp = ''
while resp != 'N':
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto R$  '))
    cont += 1
    resp = input('Deseja continuar ? [S/N] ').upper()[0].strip()

    if preco > 1000:
        maior_que_mil += 1

    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = nome

    total = total + preco

    while resp not in 'SNsn':
        resp = input('Resposta Incorreta.Digite novamente [S/N]: ').upper()[0].strip()

print('{:-^60}'.format('Fim do Programa'))

print(f'Total gasto: {total}')
print(f'Produtos que custam mais de R$1000: {maior_que_mil} ')
print(f'Produto mais barato: {barato} com um preço de {menor}')