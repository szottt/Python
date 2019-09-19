#61 MELHORE O DESAFIO 61 PERGUNTAO PARA  O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS,
# O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.

cores={
    'limpa':'\033[m',
    'vermelho':'\033[4;31m'
}
print('GERADOR DE PA')
print('-=-' * 15)
n = int(input('Digite o primeiro termo: '))
p = int(input('Digite o Razão: '))
t = n
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print('{} > '.format(t), end='')
        t += p
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('PA finalizada com {}{}{} termos visualizados'.format(cores['vermelho'],total, cores['limpa']))
