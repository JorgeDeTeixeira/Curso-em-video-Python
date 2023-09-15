# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print("Os valores sorteado foram:", end=' ')
for n in nums:
    print(f'{n}', end=' ')
print(f'\nO menor valor sorteado foi {min(nums)}.')
print(f'O maior valor sorteado foi {max(nums)}.')