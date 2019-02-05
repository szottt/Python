#45 - CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKEMPO COM VOCE.

from random import randint
from time import sleep

computador = randint(1,3)

cores = {
        'limpa':'\033[m',
        'amarelo':'\033[4;32m',
        'azul':'\033[4;34m',
        'vermelho':'\033[4;31m',
        'verde_claro':'\033[4;36m',
        'sublinhado':'\033[4m'
}

print('-=-' * 20)
print('Seja bem vindo ao Jogo virtual de JOKEMPO!!')
print('-=-' * 20)
print('''VAMOS BRINCAR ASSIM, CADA SINAL EQUIVALE A UM NUMERO:
1 - PAPEL
2 - TESOURA
3 - PEDRA''')
print('-=-' * 20)
jogador = int(input('Vamos começar, coloque o numero respectivo a sua jogada: '))
print('{}J O{}'.format(cores['verde_claro'],cores['limpa']))
sleep(1)
print('{}K E N{}'.format(cores['verde_claro'],cores['limpa']))
sleep(1)
print('{}P O{}'.format(cores['verde_claro'],cores['limpa']))
sleep(1)

if jogador == 1 and computador == 3:
    print('-=-' * 10)
    print('{}JOGADOR ESCOLHEU PAPEL E EU ESCOLHI PEDRA...{}\n'.format(cores['sublinhado'],cores['limpa']))
    print('{}DESTA VEZ VOCE GANHOU!!{}'.format(cores['azul'], cores['limpa']))
    print('\n{}Pois PAPEL ganha de PEDRA.{}'.format(cores['sublinhado'],cores['limpa']))
    print('-=-' * 10)
elif jogador == 3 and computador == 2:
    print('-=-' * 10)
    print('{}JOGADOR ESCOLHEU PEDRA E EU ESCOLHI TESOURA...{}\n'.format(cores['sublinhado'],cores['limpa']))
    print('{}DESTA VEZ VOCE GANHOU!!{}'.format(cores['azul'], cores['limpa']))
    print('\n{}Pois PEDRA ganha de TESOURA.{}'.format(cores['sublinhado'],cores['limpa']))
    print('-=-' * 10)
elif jogador == 2 and computador == 1:
    print('-=-' * 10)
    print('{}JOGADOR ESCOLHEU TESOURA E EU ESCOLHI PAPEL...{}\n'.format(cores['sublinhado'], cores['limpa']))
    print('{}DESTA VEZ VOCE GANHOU!!{}'.format(cores['azul'], cores['limpa']))
    print('\n{}Pois TESOURA ganha de PAPEL.{}'.format(cores['sublinhado'],cores['limpa']))
    print('-=-' * 10)
elif jogador == computador:
    print('-=-' * 10)
    print('\n{}E M P A T O U !!.{}'.format(cores['sublinhado'],cores['limpa']))
    print('-=-' * 10)

else:
    print('-=-' * 10)
    print('{}VOCE PERDEU! TREINE MAIS, EU SOU MUITO BOM!!!{}'.format(cores['vermelho'],cores['limpa']))
    print('-=-' * 10)

if computador == 1:
    print('O COMPUTADOR ESCOLHEU PAPEL!!')
if computador == 2:
        print('O COMPUTADOR ESCOLHEU TESOURA!!')
if computador == 3:
        print('O COMPUTADOR ESCOLHEU PEDRA!!')
 
