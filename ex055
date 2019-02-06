#55 FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS E NO FINAL MOSTRE QUEM FOI O MAIOR E QUEM FOI O MENOR PESO.


cores = {
    'limpa':'\033[m',
    'vermelho':'\033[4;31m',
    'azul':'\033[4;34m',
    'amarelo':'\033[4;32m'
}

print('-=-' * 20)
print('{:^65}'.format('Vamos ver quantos estao ganhando na {}DIETA{}'.format(cores['amarelo'], cores['limpa'])))
print('-=-' * 20)

maior = 0
menor = 0

for dieta in range(1,6):
    peso = float(input('PESO DO {}º COMPETIDOR: '.format(dieta)))
    if dieta == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O MAIOR PESO DA COMPETIÇÃO FOI DE {}{:.1f} KG{}'.format(cores['vermelho'],maior,cores['limpa']))
print('O MENOR PESO DA COMPETIÇÃO FOI DE {}{:.1f} KG{}'.format(cores['azul'],menor, cores['limpa']))


