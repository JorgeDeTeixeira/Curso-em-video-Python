# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = mais1000 = precoBarato = cont = 0
maisBarato = ' '
print('='*20)
print('LOJA SUPER BARATÃO')
print('='*20)
while True:
    prod = str(input('Nome do produto:'))
    valor = float(input('Valor do produto:'))
    cont += 1
    total += valor
    if valor > 1000:
        mais1000 += 1
    if cont == 1 or valor < precoBarato:
        maisBarato = prod
        precoBarato = valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total do valor das compras foi de R${total:.2f} reais.')
print(f'{mais1000} produtos custa mais de 1000 reais.')
print(F'{maisBarato} é o produto mais barato e custou R${precoBarato:.2f} reais.')
