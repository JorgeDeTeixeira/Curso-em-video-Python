# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro:'))
print('''Escolha a base de conversão:
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal''')
escolha = str(input('Opção:')).strip()

if escolha == '1':
    base = 'Binário'
    print(f'{num} convertido para {base}:{bin(num)[2:]}')
elif escolha == '2':
    base = 'Octal'
    print(f'{num} convertido para {base}:{oct(num)[2:]}')
elif escolha == '3':
    base = 'Hexadecimal'
    print(f'{num} convertido para {base}:{hex(num)[2:]}')
else:
    print('Escolha inválida')
