#30 CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR

numero = int(input('Digite um numero: '))
n = numero % 2
if n == 0:
    print('O seu numero é Par')
else:
    print('O seu numero é Impar')


