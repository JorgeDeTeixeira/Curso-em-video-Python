# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

nums = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))

print("Os valores sorteados foram:", end=' ')
for n in nums:
    print(f'{n}', end=' ')
print('\n')

minValue = min(nums)
maxValue = max(nums)

print(f'O menor valor sorteado foi {minValue}.')
print(f'O maior valor sorteado foi {maxValue}.')
