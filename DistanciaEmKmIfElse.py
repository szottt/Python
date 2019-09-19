#31 DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM E CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50
#POR KM PARA VIAGENS ATE 200KM E R$0,45 PARA VIAGENS MAIS LONGAS

viagem = float(input('Digite a Kilometragem da sua viagem: '))
if viagem <= 200:
    print('-=-' *20)
    print('A sua viagem fica um total de R${:.2f}, \nPois o valor de viagens abaixo de 200KM sai R$0.50 por KM rodado'.format(viagem * 0.50))
    print('-=-' *20)
else:
    print('-=-' *20)
    print('A sua viagem fica um total de R${:.2f}, \nPois o valor de viagens acima de 200KM sai R$0.45 por KM rodado'.format(viagem * 0.45))
    print('-=-' *20)
