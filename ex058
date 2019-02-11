#58 MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI PENSAR EM UM NUMERO ENTRE 0 E 10,
# SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATE ACERTAR MOSTRANDO NO FINAL
# QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER.

from random import randint
from time import sleep
n = randint(1,10)
jogador = 0
conta = 0

while jogador != n:
    jogador = int(input('Qual é a senha entre 1 a 10 :  '))
    conta += 1


    if jogador != n:
        print('HA HA HA NAO É A SENHA MAGICA...')
        sleep(1)


print('''PARABENS VOCE GANHOU EM {} TENTATIVAS!!
E A SENHA É {}!! '''.format(conta,n))
