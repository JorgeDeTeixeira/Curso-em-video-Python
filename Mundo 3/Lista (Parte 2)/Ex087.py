# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceiraColuna = 0

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valor

        if valor % 2 == 0:
            somaPares += valor

print('=' * 30)

for linha in matriz:
    for valor in linha:
        print(f'[{valor:^6}]', end='')
    print()

for linha in matriz:
    somaTerceiraColuna += linha[2]

print('=' * 30)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(
    f'O maior valor da segunda coluna é {max(matriz[0][1], matriz[1][1], matriz[2][1])}.')
