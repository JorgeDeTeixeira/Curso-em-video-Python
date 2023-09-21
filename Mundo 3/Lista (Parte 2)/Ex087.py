# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha.
matriz = [[], [], []]
valor = pares = terceiraColuna = maiorSegundaLinha = 0
for p, m in enumerate(matriz):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{p}, {c}]:'))
        matriz[p].append(valor)
        if valor % 2 == 0:
            pares += valor
print('='*30)
for p, m in enumerate(matriz):
    for c in range(0, 3):
        print(f'[{matriz[p][c]:^6}]', end='')
    print()
for l in range(0, 3):
    terceiraColuna += matriz[l][2]
print('='*30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceiraColuna}.')
print(f'O maior valor da segunda coluna é {max(matriz[1])}.')
