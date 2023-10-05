# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia(nums=[]):

    for _ in range(0, 5):
        num = randint(0, 10)
        nums.append(num)

    print('Sortendo os 5 valores da lista:', end=' ')
    for c in range(0, 5):
        print(f'{nums[c]}', end=' ')
    print('PRONTO!')


def somaPar(nums=[]):
    par = 0
    for c in range(0, 5):
        if nums[c] % 2 == 0:
            par += nums[c]

    print(f'Somando os valores pares de {nums} temos {par}')


numeros = []

sorteia(numeros)
somaPar(numeros)
