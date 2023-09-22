# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Mochila', 130, 'Caderno', 15.50, 'Estojo', 7.25, 'Caneta', 0.50, 'Livro', 25.00)

print('='*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('='*40)

for pos in range(0, len(listagem), 2):
    produto = listagem[pos]
    preco = listagem[pos + 1]
    print(f'{produto:.<30}', end=' ')
    print(f'R$:{preco:>4.2f}')

print('='*40)
