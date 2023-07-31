# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

computador = randint(0, 2)
print('''Vamos JOKENPÔ?
0 - Pedra
1 - Papel
2 - Tesoura''')
jogador = int(input('Sua opção:'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

if jogador == 0:
    if computador == 0:
        print('EMPATOU')
    elif computador == 1:
        print('VOCÊ PERDEU!') 
    else:
        print('VOCÊ GANHOU!')
elif jogador == 1:
    if computador == 0:
        print('VOCÊ GANHOU!')
    elif computador == 1:
        print('EMPATOU!')
    else:
        print('VOCÊ PERDEU!')
elif jogador == 2:
    if computador == 0:
        print('VOCÊ PERDEU!')
    elif computador == 1:
        print('VOCÊ GANHOU!')
    else:
        print('EMPATOU!')
else:
    print('OPÇÃO INVÁLIDA!')