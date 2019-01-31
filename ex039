#39 - FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE
# (SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA DELE SE ALISTAR,
# OU SE ELE JA PASSOU O TEMPO DO ALISTAMENTO)
# E TAMBEM DEVE INFORMAR QUANTO TEMPO FALTA OU QUANTO TEMPO PASSOU.


from datetime import date
from time import sleep
anoatual = date.today().year

cores = {
    'limpa':'\033[m',
    'azul':'\033[1;34m',
    'vermelho':'\033[1;31;m',
    'sublinhado':'\033[4m',
    'verificando':'\033[1;36;40m',
}

print('{}CHEGOU SUA HORA DE FAZER PARTE DO EXERCITO!!{}\n'.format(cores['sublinhado'], cores['limpa']))
idade = int(input('Digite seu ano de nascimento para verificar se ja esta apto ao serviço militar: '))
print('\n{}{}V E R I F I C A N D O {}\n'.format(cores['sublinhado'],cores['verificando'], cores['limpa']))
sleep(2)
contagem = anoatual - idade

faltante = anoatual - contagem
if contagem == 18:
    print('{}VOCE PRECISA SE ALISTAR COM URGENCIA!!{}'.format(cores['vermelho'], cores['limpa']))
elif contagem < 18:
    saldo = 18 - contagem
    print('{}VOCE AINDA NAO TEM 18 ANOS, AINDA FALTAM {} ANOS PARA SEU ALISTAMENTO!{}'.format(cores['azul'],saldo,cores['limpa']))
    ano = anoatual + saldo
    print('Seu alistamento sera daqui {} Anos.'.format(ano))

elif contagem > 18:
    saldo2 = contagem - 18
    print('{}VOCE DEVERIA TER SE ALISTADO A {} ANOS!{}'.format(cores['sublinhado'],saldo2,cores['limpa']))
    ano2 = anoatual - saldo2
    print('Seu alistamento foi a {} Anos'.format(ano2))
