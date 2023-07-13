# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite um nome completo:')).strip()

nomeLista = nome.split()
print(nomeLista)
print(f'Analisando o nome {nome}...')
print(f'Primeiro nome:{nomeLista[0]}')
print(f'Ultimo nome:{nomeLista[-1]}')