# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Informe um número e veja se ele é primo:'))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[33m', end='')
    print(f'{c} ', end='')
if cont == 2:
    print('\n\033[mEle é primo!')
else:
    print('\n\033[mEle não é primo!')
