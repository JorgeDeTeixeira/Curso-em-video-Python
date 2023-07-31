# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Valor da casa R$:'))
salarioComprador = float(input('Sálario do comprador R$:'))
anos = int(input('Em quantos anos a casa sera paga:'))

prestacao = valorCasa / (anos * 12)

print(f'Para pagar uma casa de R${valorCasa:.2f} reais em {anos} anos, a prestação será de R${prestacao:.2f} reais.')

if prestacao > salarioComprador * 30 / 100:
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO ACEITO!')