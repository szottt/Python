77) Crie um programa que tenha uma tupla com varias palavras(nao usar acentos) 
depois disso voce deve mostrar para cada palavra quais sao suas vogais

lista = ('aprender',
         'jogar',
         'brincar',
         'programar',
         'estudar',
         'andar',
         'nadar')

for p in lista:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
