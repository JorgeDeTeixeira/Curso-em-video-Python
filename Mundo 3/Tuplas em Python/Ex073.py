# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.

timesBrasileirao2021 = (
    "Flamengo",
    "Internacional",
    "Atlético Mineiro",
    "São Paulo",
    "Fluminense",
    "Grêmio",
    "Palmeiras",
    "Santos",
    "Athletico Paranaense",
    "Ceará",
    "Bragantino",
    "Corinthians",
    "Atlético Goianiense",
    "Bahia",
    "Sport Recife",
    "Fortaleza",
    "Vasco da Gama",
    "Goiás",
    "Coritiba",
    "Botafogo"
)

print('='*31)
print("Lista dos times do brasileirão:", end=' ')
for t in timesBrasileirao2021:
    print(f'{t}', end=', ')
print('')
print('='*31)
print('Os 5 primeiro colocados:', end=' ')
for t in timesBrasileirao2021[0:5]:
    print(f'{t}', end=', ')
print('')
print('='*31)
print('Os últimos 4 colocados:', end=' ')
for t in timesBrasileirao2021[16:]:
    print(f'{t}', end=', ')
print('')
print('='*31)
print(f'Em ordem alfábetica:{sorted(timesBrasileirao2021)}')
print('='*31)
