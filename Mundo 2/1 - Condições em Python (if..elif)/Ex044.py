# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Preço do produto R$:'))

print('''Forma de pagamento:
1 - à vista dinheiro/cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço formal
4 - 3x ou mais no cartão: 20% de juros''')
escolha = str(input('Digite sua opção:')).strip()

if escolha == '1':
    desconto = preco - (preco * 10 / 100)
    print(f'Preço do produto com 10% de desconto R$:{desconto:.2f} reais.')
elif escolha == '2':
    desconto = preco - (preco * 5 / 100)
    print(f'Preço do produto com 5% de desconto R$:{desconto:.2f} reais,')
elif escolha == '3':
    print(f'2 parcelas de R${preco / 2:.2f} reais.')
elif escolha == '4':
    parcelas = int(input('Quantas parcelas?'))
    juros = preco + (preco * 20 / 100)
    print(f'{parcelas} parcelas de R${juros / parcelas:.2f} reais.')
else:
    print('Opção invalida!')