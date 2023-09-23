# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

trabalhador = dict()
atual = date.today().year

trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['idade'] = atual - trabalhador['nascimento']
trabalhador['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + 35

del trabalhador['nascimento']
print('='*30)
for key, value in trabalhador.items():
    print(f'- {key} tem o valor {value}')
