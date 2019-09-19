#49 REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER SO QUE AGORA UTILIZANDO UM LAÇO FOR

print('VAMOS RELEMBRAR A ESCOLA!!')
tab = int(input('Selecione o numero que quer saber a tabuada: '))
for c in range(1, 11,):
    tabua = tab * c
    print('[{}] X [{}] = [{}]'.format(tab, c, tabua))
