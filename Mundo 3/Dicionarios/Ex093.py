# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome:'))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou:'))

for g in range(1, partidas + 1):
    gol = int(input(f'Quantos gols na partida {g}:'))
    gols.append(gol)

jogador['gols'] = gols
jogador['total'] = sum(gols)

print('='*50)
print(jogador)
print('='*50)

for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}.')
print('='*50)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for pos, g in enumerate(gols, start=1):
    print(f'=> Na partida {pos}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
