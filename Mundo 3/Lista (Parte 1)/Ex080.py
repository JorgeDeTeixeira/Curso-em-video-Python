# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
nums = []

for _ in range(0, 5):
    num = int(input('Digite um valor: '))

    if not nums or num > nums[-1]:
        nums.append(num)
        print(f'{num} foi inserido no final da lista...')
    else:
        pos = 0
        while pos < len(nums):
            if num <= nums[pos]:
                nums.insert(pos, num)
                print(f'{num} foi inserido na posição {pos}...')
                break
            pos += 1

print('=' * 30)
print(f'Os valores digitados em ordem foram {nums}')
