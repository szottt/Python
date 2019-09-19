#8 escreva um programa que leia um valor em metros e transforme em centímetros e milímetros

#metro = float(input('Digite quantos metros quer converter: '))
#print('Voce digitou {}m, e isso representa {}cm e {}mm'.format(metro, metro * 100, metro * 1000))


metro = float(input('Digite quantos metros quer converter: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
m = metro
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('Você digitou {}m e tem as seguintes medidas \n{}KM\n{}HM\n{}DAM\n{}DM\n{}CM\n{}MM'.format(m, km, hm, dam, dm, cm, mm))
