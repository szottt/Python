#42 - REFAÇA O DESAFIO 35 DOS TRIANGULOS ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIANGULO SERA FORMADO
# ( EQUILATERO, ISOSCELES DOIS LADOS IGUAIS, ESCALENO TODOS OS LADOS DIFERENTES)


from time import sleep

cores = {
    'sublinhado':'\033[4m',
    'limpa':'\033[m',
}

print('-=-' * 20)
print('Vamos criar um analisador de triangulos')
print('-=-' * 20)
l1 = float(input('Digite o primeiro segmento: '))
print('-=-' * 20)
l2 = float(input('Digite o segundo segmento: '))
print('-=-' * 20)
l3 = float(input('Digite o terceiro segmento: '))
print('-=-' * 20)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('-=-' * 13)
    print('Os segmentos PODEM formar um triangulo!')
#para fazer um if dentro de um if sempre utilize o if nao o elif
    if l1 == l2 == l3:
        print('Este triangulo é {}EQUILATERO{} pois tem todos os lados iguais'.format(cores['sublinhado'], cores['limpa']))

    elif l1 != l2 != l3 != l1:
        print('Este triangulo é {}ESCALENO!!{} pois tem todos os lados diferentes'.format(cores['sublinhado'], cores['limpa']))

    else:
        print('Este triangulo é {}Isósceles ISÓSCELES!!{} pois tem dois lados iguais'.format(cores['sublinhado'],cores['limpa']))

else:
    print('-=-' * 13)
    print('Os segmentos NAO PODEM formar um triangulo!')
    print('-=-' * 13)
