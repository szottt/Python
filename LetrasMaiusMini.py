#22 CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DA PESSOA
#1°E ELE TRAGA TODA AS LETRAS MAIUSCULAS
#2º O NOME COM TODAS AS LETRAS MINUSCULAS
#3° QUANTAS LETRAS TEM AO TODO
#4º QUANTAS LETRAS TEM O PRIMEIRO NOME

#nome = str(input('Digite seu nome completo: '))
#maiusc = nome.upper()
#minusc = nome.lower()
#cont2 = len(nome)
#separa = nome.split()
#cont3 = len(separa)
#print('O seu nome é: {}\n Maiusculas:{}\n Minusculas: {}\n Possui {} Caracteres'.format(nome, maiusc, minusc, cont3))

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras minusculas é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))) '''Melhor assim'''
