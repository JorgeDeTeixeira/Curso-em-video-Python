# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
tentativas = 0
print('Sou seu computador, vamos jogar um jogo?')
print('Estou pensando em número entre 0 e 10, tente acertar!')
jogador = int(input('Qual o seu palpite?'))
while jogador != computador:
    tentativas += 1
    if jogador > computador:
        print('Menos... Tente mais uma vez!')
        jogador = int(input('Qual o seu palpite?'))
    else:
        print('Mais... Tente mais uma vez!')
        jogador = int(input('Qual o seu palpite?'))
print(f'Acertou com {tentativas + 1} tentativas. Parabéns!')