# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

oposto = float(input('Comprimento do cateto oposto:'))
adjacente = float(input('Comprimento do cateto adjacente:'))

#hipotenusa = sqrt(pow(oposto, 2) + pow(adjacente, 2)) Uma forma
hipotesuna = hypot(oposto, adjacente)

print(f'A hipotesuna vai medir {hipotesuna:.2f}')