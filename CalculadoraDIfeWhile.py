##64 CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO QUANDO O USUARIO DIGITAR 999,
# NO FINAL MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E A SOMA ENTRE ELES, DESCONSIDERANDO O FLAG(999)


print('-=-' * 16)
print('CALCULADORA DIFERENCIADA!')
print('~' * 48)
n = 0
cont = 0
soma = 0
soma2 = 666
print(''' 
ANTES DE COMEÇAR SEGUE AS REGRAS DA CALCULADORA
1 DIGITE O NUMERO
2 CASO QUEIRA SAIR DIGITE "666"
    ''')
print('~' * 48)
while n != 666:

    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    somafi = soma- soma2


print('A sua soma dos seus numeros foi {} e voce digitou {} numeros.'.format(somafi, cont - 1))



