#vamos calular seu IMC

print('Agora vamos calcular seu IMC')
print('Um IMC(Índice de Massa Corporal) bom, deve estar entre (18,5 a 24)')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura * altura)
cores = {'limpa':'\033[4m',
         'azul':'\033[4;34m',
         'amarelo': '\033[4;33m',
         'vermelho':'\033[4;31m'}

if IMC <= 18.5:
    print('{}Abaixo do peso:{} {:.1f}'.format(cores['azul'],cores['limpa'], IMC))
elif IMC >= 18.6 and IMC < 24.9:
    print('{}Peso normal:{} {:.1F}'.format(cores['azul'],cores['limpa'], IMC))
elif IMC >= 25 and IMC < 29.9:
    print('{}Sobrepeso{}: {:.1f}'.format(cores['amarelo'], cores['limpa'], IMC))
elif IMC >= 30 and IMC < 34.9:
    print('	{}Obesidade grau 1{}: {:.1f}'.format(cores['amarelo'], cores['limpa'], IMC))
elif IMC >= 35 and IMC < 39.9:
    print('{}Obesidade grau 2{}: {:.1f}'.format(cores['vermelho'], cores['limpa'], IMC))
else:
    print('{}Obesidade grau 3{}: {:.1f}.'.format(cores['vermelho'], cores['limpa'], IMC))

