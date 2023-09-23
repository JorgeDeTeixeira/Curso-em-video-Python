# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média de {aluno["nome"]}:'))

if aluno['média'] < 4:
    aluno['situação'] = 'Reprovado'
elif 5 <= aluno['média'] <= 6:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

print('='*30)
for key, value in aluno.items():
    print(f'- {key.capitalize()} é igual a {value}.')
