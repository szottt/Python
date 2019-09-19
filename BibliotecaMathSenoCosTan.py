import math
angulo = float(input('Digite o angulo que voce quer: '))
co = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O angulo de {} tem o SENO de {:.2f}\n O angulo de {} tem o COSSENO de {:.2f}\n O angulo de {} tem a TANGENTE de {:.2f} '.format(angulo, seno, angulo, co, angulo, tan ))
