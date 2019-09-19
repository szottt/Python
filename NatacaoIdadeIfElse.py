#41 - A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM
# ATLETA E MOSTRE SUA CATEGORIA DE ACORDO COM A IDADE.
# (ATE 9 ANOS MIRIM, ATE 14 INFANTIL, ATE 19 JUNIOR, ATE 20 SENIOR E SUPERIOR MASTER.

from datetime import date
ano = date.today().year

print('Para fazer o seu cadastro na Confederação nacional de natação precisamos dos seguintes dados:')
nome = str(input('Digite seu nome: ')).strip().upper()
atleta = int(input('Digite seu ano de nascimento: '))
idade = ano - atleta
print(idade)

if idade <= 9:
    print('{}, como voce tem {} anos ou menos voce esta na categoria MIRIM!'.format(nome, idade))
elif idade <= 14:
    print('{}, como voce tem {} anos voce esta na categoria INFANTIL!'.format(nome, idade))
elif idade <= 19:
    print('{}, como voce tem {} anos voce esta na categoria JUNIOR!'.format(nome, idade))
elif idade <= 25:
    print('{}, como voce tem {} anos voce esta na categoria SENIOR!'.format(nome, idade))
else:
    print('{}, como voce tem {} anos ou mais voce esta na categoria MASTER!'.format(nome, idade))
