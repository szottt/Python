#68 faça um programa que jogue par ou impar com o computador,
# O jogo so sera interrompido quando o jogador perder

from random import randint
from time import sleep
cpu_base = randint(1,10)

color = {
        'limpa':'\033[m',
        'azul':'\033[4;34m',
        'vermelho':'\033[31m'
}

print('-*'*20)

print('{}Vamos Jogar PAR ou IMPAR!!{}'.format(color['azul'],color['limpa']))

print('-*'*20)

v = 0
while True:
        n = int(input('Digite um valor: '))
        cpu_base = randint(0, 10)
        s = n + cpu_base  # total
        tipo = ' '
        while tipo not in 'PI:':
                tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
        print('-*' * 20)
        print(f'Voce jogou {n} e o computador {cpu_base}. Total de {s} ',end='')
        print('DEU PAR' if s % 2 == 0 else 'DEU IMPAR')
        if tipo == 'P':
                if s % 2 == 0:
                        print('-*' * 20)
                        print('Voce VENCEU!')
                        print('-*' * 20)
                        v += 1
                else:
                        print('-*' * 20)
                        print('Voce PERDEU!')
                        print('-*' * 20)
                        break
        elif tipo == 'I':
                if s % 2 == 1:
                        print('-*' * 20)
                        print('Voce VENCEU!')
                        print('-*' * 20)
                        v += 1
                else:
                        print('-*' * 20)
                        print('Voce PERDEU!')
                        print('-*' * 20)
                        break
        print('Vamos jogar novamente...')
print(f'GAME OVER!! Voce venceu {v} vezes')

