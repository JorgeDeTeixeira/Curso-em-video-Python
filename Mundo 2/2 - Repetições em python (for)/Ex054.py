# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
totMaior = 0
totMenor = 0
from datetime import date
atual = date.today().year
for i in range(1, 8):
    ano = int(input(f'{i}° ano de nascimento:'))
    idade = atual - ano
    if idade < 18:
        totMenor += 1
    else:
        totMaior += 1
print(f'{totMaior} já alcançaram a maioridade.')
print(f'{totMenor} ainda não alcançaram a maioridade.')