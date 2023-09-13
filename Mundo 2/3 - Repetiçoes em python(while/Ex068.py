# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)
venceu = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(1, 10)
    total = jogador + computador
    jogada = ' '
    while jogada not in 'PIip':
        jogada = str(input('Par ou ímpar? [P/I]:')).strip().upper()[0]
    print('-'*30)
    print(
        f'Você jogou {jogador} e o computador {computador}. Total deu {total}')
    print('-'*30)
    if total % 2 == 0:
        if jogada == 'P':
            print("VOCÊ VENCEU!")
            venceu += 1
            print("VAMOS JOGAR NOVAMENTE!")
        elif jogada == 'I':
            print("VOCÊ PERDEU!")
            break
    else:
        if jogada == 'I':
            print("VOCÊ VENCEU!")
            venceu += 1
            print("VAMOS JOGAR NOVAMENTE!")
        elif jogada == 'P':
            print("VOCÊ PERDEU!")
            break
    print('-'*30)
print(F'GAME OVER! VOCÊ VENCEU {venceu} vezes.')
