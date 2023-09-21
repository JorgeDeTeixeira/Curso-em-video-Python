# # Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
nums = []
cont = 0

while True:
    resp = ' '
    nums.append(int(input('Informe um valor: ')))
    cont += 1

    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if resp == 'N':
        break

print('=' * 30)
print(f'Foram digitados {len(nums)} valores.')
nums.sort(reverse=True)
print(f'A lista ordenada de forma decrescente fica {nums}')

if 5 in nums:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

print('Fim do programa!')
