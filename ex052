#52 FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELE É OU NAO É NUMERO PRIMO.

cores={
    'vermelho':'\033[31m',
    'amarelo':'\033[33m',
    'limpa':'\033[4m'
}

print('Vamos descobrir se o numero é primo ou nao:')
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print(cores['amarelo'], end='')
        tot += 1
    else:
        print(cores['vermelho'],end='')

    print('{} '.format(c), end='')
print(cores['limpa'],'\nO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele É PRIMO!!')
else:
    print('Por isso ele NAO É PRIMO!!')
