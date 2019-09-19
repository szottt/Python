#44 - ELAGORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO
# CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO
# (A VISTA 'DINHEIRO E CHEQUE' 10%, A VISTA NO CARTAO 5%, EM ATE 2X NO CARTAO PREÇO NORMAL
# E 3X OU MAIS NO CARTAO 20% DE JUROS.

cores = {
    'limpa':'\033[m',
    'azul':'\033[4;34m',
    'amarelo':'\033[4;32m',
    'sublinhado':'\033[4m',
    'negrito':'\033[1m',
    'vermelho':'\033[4;31m'
}



print('{:=^100}'.format('SEJA BEM VINDO A NOSSA LOJA DIGITAL'))
produto = float(input('Digite o valor do produto que voce quer comprar, para informarmos em quantas vezes pode parcelar: R$ '))
print('''
Digite sua forma de pagamento:
1 - A vista 10% de desconto
2 - A vista no Cartao 5% de desconto
3 - Cheque 10% de desconto
4 - Parcelado 2x valor normal
5 - Parcelado 3x ou mais 20% de juros
''')
parametro = int(input('Qual a forma de pagamento: '))

valor1 = ((produto * 10) / 100)
valor2 = ((produto * 5 ) / 100)
valor3 = ((produto * 20 ) / 100 )
valor4 = (produto/2)
valor5 = (produto + valor3) / 2

if parametro == 1:
    print('Voce escolheu pagamento A Vista!\nDesta forma seu produto saira no valor de:{}R${:.2f}{}'.format(cores['amarelo'], produto - valor1, cores['limpa']))
elif parametro == 2:
    print('Voce escolheu pagamento A vista no Cartão!\nDesta forma seu produto saira no valor de:{}R${:.2f}{}'.format(cores['amarelo'], produto - valor2, cores['limpa'] ))
elif parametro ==3:
    print('Voce escolheu pagamento em Cheque!\nDesta forma seu produto saira no valor de:{}R${:.2f}{}'.format(cores['azul'],produto - valor1, cores['limpa']))
elif parametro == 4:
    print('Voce escolheu pagamento Parcelado em 2x \nDesta forma o valor saira no valor normal sem descontos {}R${:.2f}{} e as parcelas ficaram no valor de {}{:.2f}{}'.format(cores['azul'],produto,cores['limpa'],cores['sublinhado'],valor4,cores['limpa']))
elif parametro == 5:
    totalparcela = int(input('Quantas parcelas:'))
    parcela = (valor3 + produto) / totalparcela
    print('Voce escolheu parcelar seu pagamento e 3X ou mais \nDesta forma sera adicionado um jutos de 20% e o valor do seu produto saira {}R${:.2f}{} voce escolheu parcelar em {}X de {}R${:.2f}{}'.format(cores['vermelho'],produto + valor3,cores['limpa'],totalparcela,cores['sublinhado'],parcela,cores['limpa']))
else:
    print('\n{}OPÇÃO DE PAGAMENTO INVALIDA!{}'.format(cores['vermelho'],cores['limpa']))
    
