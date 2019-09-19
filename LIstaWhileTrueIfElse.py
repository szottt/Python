#79) Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista, 
#caso o numero ja exista la dentro, ele nao sera adicionado, 
#No final serao exibidos todos os valores unicos digitados em ordem crescente.(continuar [s/n])


#79) Crie um programa onde o usuario possa digitar varios valores numericos e
# cadastre-os em uma lista, caso o numero ja exista la dentro,
# ele nao sera adicionado, No final serao exibidos todos os valores
# unicos digitados em ordem crescente.(continuar [s/n])

lista = list()
while True:
    l = int(input('Digite um valor: '))
    if l not in lista:
        lista.append(l)
        print('Valor Adicionado com Sucesso...')
    else:
        print('Valor duplicado!')

    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'nN':
        break
print('-*' *25)
lista.sort()
print(f'Voce digitou os valores{lista}')
