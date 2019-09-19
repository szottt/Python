#59 CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NUMEROS
#[5] SAIR DO PROGRAMA

cores = {
    'limpa':'\033[m',
    'vermelho':'\033[4;31m',
    'azul':'\033[4;34m'
}

from time import sleep


n = 0
n2 = 0
esc = 0
print('-=-' * 20)
print('Vamos montar nossa primeira calculadora!')
while esc != 5:
    print(''' O QUE DESEJA FAZER
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA''')

    n = int(input('Digite o {}1º{} numero: '.format(cores['azul'], cores['limpa'])))
    n2 = int(input('Digite o {}2º{} numero: '.format(cores['vermelho'], cores['limpa'])))
    esc = int(input('Digite a opção que quer realizar: '))
    if esc == 1:
        soma = n + n2
        print('A soma dos numeros {} e {} é {}'.format(n, n2, soma))
    if esc == 2:
        multi = n * n2
        print('A multiplicação dos numeros {} e {} é {}'.format(n, n2, multi))
    if esc == 3:
        if n > n2:
            print('O numero {} é maior que {}'.format(n,n2))
        else:
            print('O numero {} é maior que {}'.format(n2, n))
    if esc  == 4:
        print('Voce escolheu a opção {} entao volte e escolha novos numeros.'.format(esc))
        sleep(1)

print('-=-' * 20)
print('{}VOCÊ SAIU DO PRORAMA{}'.format(cores['vermelho'], cores['limpa']))
