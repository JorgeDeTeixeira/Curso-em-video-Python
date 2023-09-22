# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
nums = (
    int(input('Informe um número: ')),
    int(input('Informe outro número: ')),
    int(input('Informe mais um número: ')),
    int(input('Informe o último número: '))
)

print(f'Você digitou os valores {nums}')

count9 = nums.count(9)
print(f'O valor 9 apareceu {count9} vezes.')

if 3 in nums:
    index3 = nums.index(3) + 1
    print(f'O número 3 foi digitado pela primeira vez na posição {index3}.')
else:
    print('O número 3 não foi informado!')

pares = sum(1 for num in nums if num % 2 == 0)
print(f'Os valores pares digitados foram {pares}')
