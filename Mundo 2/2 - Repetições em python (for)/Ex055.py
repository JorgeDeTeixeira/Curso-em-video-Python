# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maiorPeso = 0
menorPeso = 0
for p in range(1, 6):
    peso = float(input(f'Informe o {p}° peso:'))
    if p == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print(f'Menor peso:{menorPeso}')
print(f'Maior peso:{maiorPeso}')