#78) Faça um programa que leia 5 valores numericos e guardeos em uma lista,
# no final mostre qual foi o maior e o menor valor e as suas respectivas posiçoes na lista.
'''
lista = [int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: '))]
'''
lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]



print(f'Voce Digitou os valores: {lista}')
print(f'O maior valor foi {maior} nas posicoes ',end='')
for i, v in enumerate(lista):
    if lista[i] == maior:
        print(f'{i}...',end = '')
print()
print(f'O menor valor foi {menor} nas posicoes ',end='')

for i,v in enumerate(lista):
    if lista[i] == menor:
        print(f'{i}...',end='')
