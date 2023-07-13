# #Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo:')).strip()

primeiro = nome.split()

print('Analisando seu nome...')
print(f'Nome em maiusculo:{nome.upper()}')
print(f'Nome em minúsculo:{nome.lower()}')
print(f'Quantas letras ao todo:{len(nome) - nome.count("")}')
print(f'O primeiro nome tem {len(primeiro[0])} letras')
#print(f'O primeiro nome tem {nome.find(" ")} letras')  # Outra forma de fazer
