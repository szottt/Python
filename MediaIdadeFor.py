#56 DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS, NO FINAL DO PROGRAMA MOSTRE
#A MEDIA DE IDADE DO GRUPO
#QUAL O NOME DO HOMEM MAIS VELHO
#QUANTAS MULHERES TEM MENOS DE 20 ANOS

cores = {
    'limpa':'\033[m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'sub':'\033[4m'
}

soma = 0
media = 0
maioridadehome = 0
nomevelho = 0
totmulher20 = 0

for c in range(1,5):
    print('-=-' * 20 )
    print('{}º -PESSOA-'.format(c))
    n = str(input('NOME: ')).strip()
    i = int(input('IDADE: '))
    s = str(input('SEXO [M/F]: ')).strip()
    soma += i

    if c == 1 and s in 'Mm':
        maioridadehome = i
        nomevelho = n
    if s in 'Mm' and i > maioridadehome:
        maioridadehome = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        totmulher20 += 1

media = soma / c

print('A MEDIA DE IDADE É: {}'.format(media))
print('O Homem mais velho tem {} anos e se chama {}.'.format(maioridadehome,nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos.'.format(totmulher20))
