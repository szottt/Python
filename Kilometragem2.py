#15 Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado, calcule o preço a pagar sabendo que
#o carro custa 60 por dia e 0,15 por km

dias = int(input('Quantos dias voce ficou com o carro: '))
km = float(input('Quantos KM voce percorreu com o carro: KM '))
calcdias = (dias * 60)
calckm = km * 0.15
calcfinal = calcdias + calckm
print('Seu cartao sera tarifado com o valor de R${:.2f} devido a ter gasto R${:.2f} em dias e R${:.2f} em Km rodados'.format(calcfinal, calcdias, calckm))





# 60 POR DIA E 0,15 POR KM
