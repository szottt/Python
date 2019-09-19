#69 crie um programa que leia a idade e o sexo de varias pessoas,
# a cada pessoa cadastrada o programa devera perguntar se o
# usuario quer ou nao quer continuar, no final mostre:

#A Quantas pessoas tem mais de 18 anos.
#B Quantos homens foram cadastrados.
#C Quantas mulheres tem menos de 20 anos.

from time import sleep
from datetime import date
anoatual = date.today().year


CORES = {'LIMPA':'\033[m',
'AMARELO':'\033[4;33m',
'VERDE':'\033[4:32m',
'VERMELHO':'\033[4;31m'}

print("-*"* 20)
print('Bem vindo ao cadastros de clientes da loja do IGOR!')

cont = cont2 = cont3 = idade = contagem_ini =0

while True:

        print("-*" * 20)
        print('CADASTRE UMA PESSOA!')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
            print('Digite novamente')
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
        print('{}C A D A S T R A N D O . . .{}'.format(CORES['VERMELHO'], CORES['LIMPA']))
        sleep(1)
        contagem_ini += 1

        if idade >= 18:
            cont += 1

        if sexo == 'M':
            cont2 += 1

        if sexo == 'F':
            if idade <= 20:
                    cont3 += 1

        #if sexo == 'F' and idade <= 20:
        #   cont2 +=1

        if continuar == 'N':
            print('{}E\nF I N A L I Z A N D O . . . {}'.format(CORES['VERMELHO'], CORES['LIMPA']))
            sleep(1)
            break


print(f'Tivemos um total de {cont} pessoas com mais de 18 anos!')
print(f'E ao todo tivemos {cont2} homens cadastrados e {cont3} mulheres com menos de 20 anos!')
