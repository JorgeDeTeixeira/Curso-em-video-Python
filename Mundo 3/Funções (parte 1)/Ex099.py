# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* nums):
    maior = 0

    print('='*40)
    print('Analisando os valores passados...')
    for c, n in enumerate(nums):
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)

    print(f'Foram informados {len(nums)} valores ao todo.')

    for c, n in enumerate(nums):
        if c == 0:
            maior = n
        else:
            if n > maior:
                maior = n

    if len(nums) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {maior}.')


maior(2, 4, 9, 5, 2)
maior()
