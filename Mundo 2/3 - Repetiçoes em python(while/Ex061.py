# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('GERADOR DE PA')
print('='*20)
p1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))
cont = 1
while cont < 11:
    print(f'{p1} -> ', end='')
    p1 += r
    cont += 1
print('FIM')
