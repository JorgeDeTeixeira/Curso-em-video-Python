# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)

title = 'jogo da adivinhação'.upper()
print(f'{title:=^50}')
jogador = int(input('Tente adivinhar qual número eu pensei entre 0 e 5:'))
print('PROCESSANDO...')
sleep(1.5)

if (computador == jogador):
    print('VOCÊ GANHOU ):')
else:
    print(f'VOCÊ PERDEU, PENSEI NO {computador} E NÃO NO {jogador} (:')

#print('VOCÊ GANHOU (:' if computador == jogador else 'VOCÊ PERDEU ):') Versão simplificada