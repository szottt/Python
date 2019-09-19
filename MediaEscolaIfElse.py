#40 - CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A MEDIA
# (<5 REPROVADO 5 A 6.9 RECUPERAÇÃO 7 OU SUPERIOR APROVADO)
from random import randint
from time import sleep
cores = {
    'limpa':'\033[m',
    'azul':'\033[1;34m',
    'vermelha':'\033[1;31m',
    'sublinhado':'\033[4m',
}
print('{}Chegou o final do ano e precisamos verificar passou de ano!{}'.format(cores['sublinhado'], cores['limpa']))
nome = str(input('Nos diga seu nome e vamos informar sua nota: ')).strip().upper()

ra = randint(1000, 5000)

n1 = float(input('Digite sua nota do {}primeiro semestre{} '.format(cores['sublinhado'], cores['limpa'])))
n2 = float(input('Digite sua nota do {}segundo semestre{} '.format(cores['sublinhado'], cores['limpa'])))

print('\n{}V E R I F I C A N D O{}\n'.format(cores['sublinhado'], cores['limpa']))
media = (n1 + n2) / 2

print('-#-' * 10)

print('Aluno {} com o RA {}:'.format(nome, ra))


if media < 5:
    print('{}VOCE FOI REPROVADO, POIS FICOU COM {} DE MEDIA{}'.format(cores['vermelha'],media, cores['limpa']))
    print('-#-' * 10)
elif media >= 5 and media <= 6.9:
    print('{} VOCE ESTA DE RECUPERAÇÃO, POIS FICOU COM {} DE MEDIA{}'.format(cores['sublinhado'],media,cores['limpa']))
    print('-#-' * 10)
else:
    print('{}{}VOCE FOI APROVADO,POIS FICOU COM {} DE MEDIA, PARABENS!!{}'.format(cores['sublinhado'],cores['azul'],media,cores['limpa']))
    print('-#-' * 10)
