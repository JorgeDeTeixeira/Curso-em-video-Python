# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou:'))

    gols = []
    total_gols = 0

    for g in range(1, partidas + 1):
        gol = int(input(f'Quantos gols na partida {g}: '))
        gols.append(gol)
        total_gols += gol

    jogador['gols'] = gols
    jogador['total'] = total_gols

    jogadores.append(jogador)

    resp = input('Quer continuar [S/N]? ').strip().upper()[0]
    if resp != 'S':
        break

print('='*60)
print(f'{"Código":<6} {"Nome":<15} {"Gols":<25} {"Total de Gols":<15}')
print("="*60)

for indice, jogador in enumerate(jogadores):
    codigo = indice
    nome = jogador["nome"]
    gols = " ".join(map(str, jogador["gols"]))
    total_gols = jogador["total"]

    print(f'{codigo:<6} {nome:<15} {gols:<25} {total_gols:<15}')
print('='*60)

while True:
    dado = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dado == 999:
        break

    if dado < 0 or dado >= len(jogadores):
        print('ERRO! Índice não encontrado!')
    else:
        print('='*60)
        print(f'Levantamento do jogador {jogadores[dado]["nome"]}:')
        for i, g in enumerate(jogadores[dado]["gols"]):
            print(f'No jogo {i+1} fez {g} gols.')
        print('='*60)
print('PROGRAMA ENCERRADO!')
