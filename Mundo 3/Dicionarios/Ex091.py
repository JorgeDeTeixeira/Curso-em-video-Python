# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter


def lancarDados():
    return randint(1, 6)


jogadas = {}

for jogador in range(1, 5):
    resultado = lancarDados()
    jogadas[f'Jogador {jogador}'] = resultado

for jogador, jogada in jogadas.items():
    print(f'{jogador} tirou {jogada} no dado.')
    sleep(1)

ranking = []

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('='*30)
print(f'{"RANKING":^30}')
print('='*30)
for i, v in enumerate(ranking):
    print(f'Jogador {i+1} lugar:{v[0]} com {v[1]}')
    sleep(1)
