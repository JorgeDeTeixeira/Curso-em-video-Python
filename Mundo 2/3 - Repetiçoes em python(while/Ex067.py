# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Digite um número para ver a tabuada:'))
    if num < 0:
        break
    print(f'Tabuada de {num}')
    print('='*20)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('='*20)
print('PROGRAMA DA TABUADA ENCERRADO! VOLTE SEMPRE!')