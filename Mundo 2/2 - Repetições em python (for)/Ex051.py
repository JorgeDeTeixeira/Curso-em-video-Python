# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
dez = primeiro + 10 * razao

for c in range(primeiro, dez, razao):
    print(c, end=' -> ')
print('FIM')
