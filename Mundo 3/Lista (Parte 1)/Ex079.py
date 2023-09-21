# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
nums = []
nums = []

while True:
    num = int(input('Digite um valor: '))

    if num not in nums:
        nums.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar...')

    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if resp == 'N':
        break

print('=' * 30)
nums.sort()
print(f'Você digitou os valores {nums}')
