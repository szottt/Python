#67 faça um programa que mostre a tabuada de varios numeros,
# um de cada vez para cada valor digitado e sera interrompido quando um numero
# negativo for solicitado

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))

    if n < 0:
        break

    print('-/'*30)

    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')

    print('-/' * 30)

print('Neste programa nao se pode usar numero negativo, volte sempre!')
