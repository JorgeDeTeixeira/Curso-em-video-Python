# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantidade de dias alugados:'))
km = float(input('Quantidade de KM pecorridos:'))

tittle = 'RECIBO'
tDias = dias * 60
tKm = km * 0.15

print(f'{tittle:=^60}')
print(f'Total de dias alugados:{dias} | Quantidade de KM rodados:{km:.2f}')
print(f'Valor por dia alugado R$:{tDias:.2f} | Valor por KM rodado:{tKm:.2f}')
print(f'Valor total R$:{tDias + tKm:.2f}')
