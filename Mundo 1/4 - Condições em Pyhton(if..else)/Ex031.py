# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Digite a distância da viagem:'))

# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(
    f'O valor da sua passagem ficou de R$:{preco:.2f} reais.')
