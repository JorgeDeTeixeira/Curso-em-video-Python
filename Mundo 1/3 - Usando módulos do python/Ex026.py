# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase:')).strip().upper()

print(f'Quanta vezes aparece a letra "A":{frase.count("A")}')
print(
    f'A letra "A" aparece pela primeira vez na posição:{frase.find("A") + 1}')
print(f'A letra A aparece pela última vez na posição:{frase.rfind("A") + 1}')
