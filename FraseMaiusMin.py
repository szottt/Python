#nome = str(input('Digite uma frase: ')).strip()
#nome.lower()
#a = nome.count('A')
#pos = nome.find('A')
#print('{} e {}'.format(a, pos))

frase = str(input('Digite uma frase: ')).upper().strip()
print('A sua frase tem {} letras A'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))
