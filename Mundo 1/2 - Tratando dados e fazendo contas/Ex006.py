from math import sqrt

num = int(input('Digite um número:'))

print(f'O dobro de {num} é {num * 2}.')
print(f'O triplo de {num} é {num * 3}.')
print(f'A raíz quadrada de {num} é {sqrt(num):.2f}.')  # Usando biblioteca
# print(f'A raíz quadrada de {num} é {num ** (1/2)}.') ##Usando **
