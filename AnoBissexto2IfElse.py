#37 - ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER
# QUAL SERA A BASE DE CONVERSAO: (1 PARA BINARIO, 2 PARA OCTAL 3 PARA HEXADECIMAL)

numero = int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero)))

elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)))

else:
    print('Opção invalida!!')
