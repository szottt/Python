#80) Crie um programa onde o usuario possa digitar 5 valores numericos e 
#cadastre-os na inserção (sem usar o sort()) no final mostre a lista ordenada na tela


lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao Final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos +=1
print('-*' * 30)
print(f'Os valores digitados em ordem foram {lista} ')
