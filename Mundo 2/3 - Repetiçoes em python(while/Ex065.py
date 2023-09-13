# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
media = cont = maior = menor = 0
resp = ''
while resp != 'N':
    num = int(input('Digite um número:'))
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    media += num
    resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
print(f'Você digitou {cont} números e a média foi {media / cont}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
