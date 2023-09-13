# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*35)
print('{:^30}'.format('BANCO DA GUANABARA'))
print('='*35)
valor = int(input('Quanto você quer sacar R$:'))
valorTotal = valor
cedula = 100
totalCedulas = 0
while True:
    if valorTotal >= cedula:
        valorTotal -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} notas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if valorTotal == 0:
            break
