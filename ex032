#32 DESENVOLVA UM PROGRAMA QUE MOSTRE SE O ANO É BISSEXTO.

from datetime import date

ano = int(input('Digite um ano e veja se ele é Bissexto ou coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year #pega o ano atual configurado na maquina

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto:'.format(ano))
else:
    print('O ano {} nao é Bissexto'.format(ano))


