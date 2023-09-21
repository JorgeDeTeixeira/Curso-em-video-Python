from time import sleep
from random import randint
jogo = list()
megaSena = list()
print('='*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('='*30)
quantos = int(input('Quantos jogos você quer que eu sorteie? '))
print('='*6, f'SORTEANDO {quantos} JOGOS', '='*6)
for c in range(0, quantos):
    while True:
        if len(jogo) >= 6:
            break
        valor = randint(1, 60)
        if valor not in jogo:
            jogo.append(valor)
    jogo.sort()
    megaSena.append(jogo[:])
    jogo.clear()
for p, m in enumerate(megaSena):
    print(f'Jogo {p + 1}: {megaSena[p]}')
    sleep(1)
