#70  crie um programa que leia o nome e o preço de varios produtos.
#O programa devera perguntar se o usuario vai continuar,
# no final mostre assim:
#A qual o total de gastos da compra
#B Quantos produtos custam mais de R$1000
#C Qual é o nome do produto mais barato.

totalmil = total_produtos = cont = maior = quant = menor = 0

print('-*' * 20)
print('{:^40}'.format('LOJA BARATA!!'))
print('-*' * 20)
while True:
    produto = str(input('Nome do produto? ')).strip().upper()
    valor = float(input('Qual o valor? R$ '))
    quant += 1
    total_produtos += valor

    if valor > 1000:
        totalmil += 1

    if quant == 1 or valor < menor:
        menor = valor
        barato = produto

    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if seguir == 'N':
        break


print(f'O Total da sua compra foi de{total_produtos:10.2f}')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
print(f'Teve {totalmil} produtos que foram mais de R$1000.00')

