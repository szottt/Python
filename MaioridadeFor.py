#54 CRIE UM PROGRAMA QUE LEIA O ANO NASCIMENTO DE SETE PESSOAS.
# NO FINAL MOSTRE QUANTAS PESSOAS AINDA NAO ATINGIRAM A MAIORIDADE E QUANTAS JA SAO MAIORES (21 ANOS).

from datetime import date

anoatual = date.today().year

print('-=-' * 20)
print('{:^50}'.format('VAMOS BRINCAR COM IDADES!'))
print('-=-' * 20)

totmenor = 0
totmaior = 0

for c in range(1, 8):
    idade = int(input('EM QUE ANO A {}º PESSOA NASCEU: '.format(c)))
    contagem = anoatual - idade

    if  contagem <= 21:
        totmenor += 1
    else:
        totmaior += 1

print('O numero de pessoas com menos de 21 anos é {}'.format(totmenor))
print('O numero de pessoas com idade supediror a 21 é {}'.format(totmaior))

