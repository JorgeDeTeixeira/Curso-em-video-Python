# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for p, m in enumerate(matriz):
    for c in range(0, 3):
        matriz[p].append(int(input(f'Digite um valor para [{p}, {c}]:')))
    print(matriz[p][c])
print('='*30)
for p, m in enumerate(matriz):
    for c in range(0, 3):
        print(f'[{matriz[p][c]:^6}]', end='')
    print()

