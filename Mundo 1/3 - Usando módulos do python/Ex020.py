# mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')

ordem = [a1, a2, a3, a4]
shuffle(ordem)
print('A ordem de apresentação será')
print(ordem)