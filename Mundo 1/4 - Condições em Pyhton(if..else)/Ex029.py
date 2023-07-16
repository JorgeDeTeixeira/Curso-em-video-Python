# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade do carro KM:'))

if (velocidade > 80):
    multa = (velocidade - 80) * 7
    print(
        f'Você ultrapassou a velocidade permitida de 80km/h, sua multa foi de R$ {multa:.2f} reais!')
print('Tenha um bom dia!, Dirija com cuidado!')
