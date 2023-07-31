# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro:'))

print('''Escolha a base de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal''')
escolha = str(input('Opção:')).strip()

if escolha == '1':
      base = 'Binário'
      conversao = bin(num)
elif escolha == '2':
      base = 'Octal'
      conversao = oct(num)
elif escolha == '3':
      base = 'Hexadecimal'
      conversao = hex(num)
else:
      print('Escolha inválida')

print(f'{num} convertido para {base}:{conversao[2:]}')