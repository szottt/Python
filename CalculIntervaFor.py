#48 FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLOS DE TRES
#E QUE SE ENCONTRAM NO INTERVALO DE 1 ATE 500.

from time import sleep

cores = {
    'limpa':'\033[m',
    'sublinhado':'\033[4m',
    'azul':'\033[4;34m'

}

#IMPAR = DIVIDE POR 2 E RESTA 1
#DIVISIVEL POR 3 E QUANDO SE DIVIDE POR TRES E FICA COM O RESTO = 0

print('VAMOS DESCOBRIR QUAIS SAO OS NUMEROS IMPARES DIVISIVEIS POR 3 NO INTERVALO SELECIONADO')
inter1 = int(input('Selecione o inicio do intervalo: '))
inter2 = int(input('Selecione o final do intervalo:'))
for c in range(inter1, inter2):
    i = c % 2
    d = c % 3
    if i == 1:
        if d == 0:
            print('{}{}{}'.format(cores['azul'],c,cores['limpa']))
            sleep(0.5)
print('Estes sao os numeros impares e multiplos de 3')
