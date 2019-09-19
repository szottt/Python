#47 CRIE UM PROGRAMA QUE MSOTRE NA TELA TODOS OS NUMEROS PARES QUE ESTAO EM UM INTERVALO DE 1 E 50.


print('Vamos descobrir quais os numeros sao pares entre 0 e 50!')
for c in range(0,50):
    p = c % 2
    if p == 1:
        print(c)

print('TEMOS A LISTAGEM DE NUMEROS PARES ACIMA!')
