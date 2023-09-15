# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
nums = (int(input(f'Informe um número:')), int(input(f'Informe outro número:')), int(
    input(f'Informe mais um número:')), int(input(f'Informe o último número:')))
print(f'Você digitou os valores {nums}')
print(f'Apereceu {nums.count(9)} vezes o valor 9.')
if 3 in nums:
    print(
        f'O número 3 foi digitado a primeira vez na posição {nums.index(3) + 1}.')
else:
    print('O número 3 não foi informado!')
pares = 0
for c in range(0, 4):
    if nums[c] % 2 == 0:
        pares += 1
print(f'Os valores pares digitados foram {pares}')
