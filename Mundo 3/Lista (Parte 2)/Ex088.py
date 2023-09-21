from time import sleep
from random import randint

jogos = []
megaSena = []

print('=' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('=' * 30)

quantidadeJogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('=' * 6, f'SORTEANDO {quantidadeJogos} JOGOS', '=' * 6)

for _ in range(quantidadeJogos):
    jogo = []

    while len(jogo) < 6:
        numero = randint(1, 60)

        if numero not in jogo:
            jogo.append(numero)

    jogo.sort()
    jogos.append(jogo)

for indice, jogo in enumerate(jogos):
    print(f'Jogo {indice + 1}: {jogo}')
    sleep(1)
