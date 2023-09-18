# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
nums = []
for c in range(0, 5):
    num = nums.append(int(input(f'Informe o {c + 1}° valor:')))

maior = menor = posMaior = PosMenor = 0
for c in range(0, len(nums)):
    if c == 0:
        maior = menor = nums[c]
        posMaior = PosMenor = c
    else:
        if nums[c] > maior:
            maior = nums[c]
            posMaior = c
        if nums[c] < menor:
            menor = nums[c]
            PosMenor = c
print(f'Você digitou os valores {nums}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(nums):
    if v == maior:
        print(f'{i + 1}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(nums):
    if v == menor:
        print(f'{i + 1}...', end=' ')
