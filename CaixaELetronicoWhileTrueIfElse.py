#71 Crie um programa que simule o funcionamento de um caixa eletronico.
#No incio pergunte ao usuario qual sera o valor a ser sacado,
# O programa deve informar quantas celulas de cada valor vao ser entregues.
#obs: considere que o caixa possui cedulas de R$ 50 R$ 20 R$ 10 R$ 5


print('-*' * 25)
print('{:^40}'.format('Caixa Eletronico'))
print('-*' * 25)
print('''CÉDULAS DISPONIVEIS:
R$ 100
R$ 50
R$ 20
R$ 10
R$ 05
R$ 01
''')
print('-*' * 25)
valor = int(input('Qual valor gostaria de sacar? R$'))
total = valor
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced >0:
            print(f'Total de {totalced} cedulas de R${ced:.2f}')

        elif ced == 100:
            ced = 50

        elif ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 5

        elif ced == 5:
            ced = 1

        totalced = 0
        if total == 0:
            break
print('-*' * 20)
print('{:^40}'.format('Volte sempre ao meu banco!'))
print('-*' * 20)
