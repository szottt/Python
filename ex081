#81) Crie um programa que vai ler varios numeros e colocar em uma lista, depois disso mostre:
#A) Quantos numeros foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e esta ou nao na lista.
#(continuar [s/n])



list = list()
while True:
    list.append(int(input('Digite um valor: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]

    if resposta in "nN":
        break
print(f'Voce digitou {len(list)} elementos')
list.sort(reverse=True)
print(f'Os valores em ordem decrescente são {list}')
if 5 in list:
    print(' O valor 5 faz parte na lista!')
else:
    print('O valor 5 não faz parte da lista!')
