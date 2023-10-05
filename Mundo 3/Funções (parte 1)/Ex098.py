# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
from time import sleep


def linha():
    print('='*30)


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')

    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    if inicio < fim:
        cont = inicio
        linha()
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')
        linha()
    else:
        cont = inicio
        linha()
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')
        print("="*30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez, personalize sua contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
