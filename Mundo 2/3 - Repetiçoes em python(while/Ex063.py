# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termos = int(input('Quantos termos você quer mostrar:'))
cont = 0
t1 = 0
t2 = 1
t3 = 0
print('-'*30)
while cont < termos:
    cont += 1
    print(f'{t3}', end='')
    print(' -> ' if cont < termos else ' FIM ', end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
