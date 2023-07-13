salario = float(input("Digite seu sálario R$:"))

aumento = salario * 15 / 100
title = 'SÁLARIO'

print(f'{title:=^25}')
print(f'Sálario R$:{salario:.2f} \nValor do aumento R$:{aumento:.2f} \nNovo sálario R$:{salario + aumento:.2f}.')
print(f'{title:=^25}')
