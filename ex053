#53 CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDROMO.
#EX: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper() #strip tirou os espaços antes e depois
palavras = frase.split() #separou em partes
junto = ''.join(palavras) #juntou tudo e tirou os espaços internos
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('Voce digitou a frase {}'.format(junto))
print('Desta forma ao contrario fica {}'.format(inverso))
if inverso == junto:
    print('TEMOS UM PALINDROMO')
else:
    print('NÃO TEMOS UM PALIDROMO')

