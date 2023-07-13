# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o nome de uma pessoa:')).upper().strip()
print(f'Seu nome tem silva? {"SILVA" in nome}')