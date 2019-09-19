import random
n1 = str(input('Digiete o primeiro Aluno: '))
n2 = str(input('Digite o segundo Aluno: '))
n3 = str(input('Digite o terceiro Aluno: '))
n4 = str(input('Digite o quarto Aluno: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print('A ordem da apresentação sera: {}'.format(lista))
