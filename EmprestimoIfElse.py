#36 - ESCREVA UM PROGRAMA QUE APROVE UM EMPRESTIMO BANCARIO
#PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR
#DA CASA O SALARIO E EM QUANTOS ANOS ELE VAI PAGAR (CALCULE
#O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NAO PODE
#EXCEDER 30% DO SALARIO OU ENTAO O EMPRESTIMO SERA NEGADO.

cores = {
    'limpa':'\033[m',
    'vermelho':'\033[1;31m',
    'azul':'\033[1;34m',
    'negrito':'\033[1m',
    'sublinhado': '\033[4m',
    'amarelo': '\033[4;33m',
}

from time import sleep
print('Bem vindo a Caixa Economica!')
casa = float(input('Qual é o valor do imovel Senhor/a? R$ '))
salario = float(input('Por favor nos informe o seu salario bruto: R$'))
tempo = int(input('Em quantos anos voce gostaria de pagar: '))

tempo2 = tempo * 12
mensalidade = ((salario * 30) /100)
prestacao = (casa / tempo2)


print('{}C A L C U L A N D O{}\n'.format(cores['amarelo'], cores['limpa']))
sleep(2)

if mensalidade < prestacao:
    print('{}Voce nao pode fazer o financiamento!!\n{}'.format(cores['vermelho'],cores['limpa']))
    print('{}Pois o valor da sua renda ou a quantidade de parcelas escolhidas nao foi o suficiente\n'
          'Pois temos uma politica que todo financiamento nao pode ser inferior a 30% do salario.{}'.format(cores['negrito'], cores['limpa']))
else:
    print('{}Parabens seu Financiamento foi {}A P R O V A D O{}\n\n'
          'O seu financiamento com o valor de R${:.2f}, no valor de R${:.2f} em {} parcelas. '.format(cores['negrito'], cores['azul'],cores['limpa'], casa, prestacao, tempo))

