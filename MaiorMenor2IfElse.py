#38 - ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS E COMPARE QUAL É O MAIOR, MENOR OU IGUAL


cores = {
    'limpa': '\033[m',
    'negrito': '\033[1;m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;32m'
}

print('{}Vamos fazer um desafio, voce me fala dois numeros e eu te respondo qual seria maior!!{}'.format(cores['negrito'],cores['limpa']))
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O {}PRIMEIRO{} numero é maior'.format(cores['azul'],cores['limpa']))
elif n2 == n1:
    print('{}Os numeros sao iguais{}'.format(cores['negrito'], cores['limpa']))
else:
    print('O {}SEGUNDO{} numero é maior'.format(cores['amarelo'], cores['limpa']))
