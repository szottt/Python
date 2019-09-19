import math
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto: '))
h1 = math.hypot(co, ca)
print('a hipotenusa mede {:.2f}'.format(h1))



'''co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
