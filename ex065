#65 CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO E NO FINAL MOSTRE A MEDIA ENTRE TODOS
# OS VALORES E QUAL FOI O MAIOR E O MENOR VALOR LIDO,
# O PROGRAMA DEVE PERGUNTAR SE O USUARIO QUER OU NAO CONTINUAR (S OU N)

resp = 'S'
soma = quant = media = maior = menor =0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()

media = soma / quant

print('Voce digitou {} numeros e a media desses numeros foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
