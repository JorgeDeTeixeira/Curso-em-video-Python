# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('APRENDER', 'ANDAR', 'OI', 'CORRER', 'CURSO', 'MERCARDO')

for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for v in range(0, len(p)):
        if p[v] in 'AEIOU':
            print(p[v], end=' ')
