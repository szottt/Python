#75) Desenvolva um programa que leia quatro valores, pelo teclado e guarde-os em uma tupla.
# No final mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os numeros pares.

val = (int(input('Digite o primeiro numero: ')),int(input('Digite o segundo numero: ')),
       int(input('Digite o quarto numero: ')),int(input('Digite o quinto numero: ')))

print('Os valores digitados são: ', end='')
for v in val:
    print(f'{v} ', end='')

if 9 in val:
    print(f'\nO numero 9 apareceu: {val.count(9)} vezes.')
else:
    print('\nO numero 9 nao foi digitado.')

if 3 in val:
    print(f'O numero 3 foi digitado na posição : {val.index(3)+1}ª posição.')
else:
    print('O valor 3 nao foi digitado.')


print('Os valores pares digitados foram: ', end='')

for valor in val:
    if valor % 2 == 0:
        print(valor, end=' ')
