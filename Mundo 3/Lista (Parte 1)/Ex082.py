# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
nums = []
pares = []
impares = []

while True:
    resp = ' '
    nums.append(int(input('Informe um valor: ')))

    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if resp == 'N':
        break

print(f'A lista completa é {nums}.')

for n in nums:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()

print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
