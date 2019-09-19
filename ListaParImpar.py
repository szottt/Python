#82) Crie um programa que leia varios numeros e colocar em uma lista, depois disso
# crie duas listas extras que vao conter apenas valores pares e os valores impares digitados
# respectivamente, Ao final mostre conteudo das tres listas geradas.(continuar [s/n])


lista_par = list()
lista_impar = list()
lista = list()

while True:

    print('*-' *15)
    n = int(input('Digite um numero: '))
    print('*-' *15)
    lista.append(n)

    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]

    if continuar in 'Nn':
        break
    lista_impar.sort()
    lista_par.sort()
    lista.sort()

print('-*' * 25 )
print(f'A lista completa é {lista}')
print(f'A lista com os numeros Pares é {lista_par}')
print(f'A lista com os numeros Impares é {lista_impar}')
print('-*' * 25)
