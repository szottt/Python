#73 Crie uma tupla preenchida com os 20 primeiros numeros colocados da tabela do campeonato brasileiro
# de futebol, na ordem de colocação. depois mostre.
#a) Apenas os 5 primeiros colocados
#b) Os ultimos 4 colocados
#c) Uma lista com os times em ordem alfabetica
#d) Em que posicao na tabela esta o time da Chapecoense.

times = ('Atlético-MG','Avaí','Bahia','Botafogo','CSA',
         'Ceará','Chapecoense','Corinthians','Cruzeiro',
         'Flamengo','Fluminense','Fortaleza','Goiás',
         'Grêmio','Internacional','Palmeiras','Santos',
         'São Paulo','São Paulo','Vasco')

print('TIMES DO CAMPEONATO BRASILEIRO 2018!!')

print('-*'*30)
print(f'Os times são esses:\n{times}\n')
print('-*'*30)
print(f'Os Quatro primeiros times do Campeonato são:\n{times[0:4]}\n')
print('-*'*30)
print(f'Os Cinco ultimos times do Campeonato são:\n{times[-5:]}\n')
print('-*'*30)
print(f'Na ordem Alfabetica os times ficam da seguinte forma:\n{sorted(times)}\n')
print('-*'*30)
print(f'O Chapecoense esta na posição {times.index("Chapecoense")+1}ª posição')
