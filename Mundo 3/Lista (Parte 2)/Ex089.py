# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = [[], [], []]
notas = []
while True:
    alunos[0].append(str(input('Nome:')))
    for c in range(1, 3):
        nota = float(input(f'Nota {c}°:'))
        notas.append(nota)
    alunos[1].append(notas[:])
    alunos[2].append(sum(notas) / 2)
    notas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    if resp == 'N':
        break
print('='*30)
print(f'{"No.":<4} {"NOME":<10}{"MÉDIA":>8}')
print("="*30)
for p in range(len(alunos[0])):
    print(f'{p:<4} {alunos[0][p]:<10}{alunos[2][p]:>8}')
print("=" * 30)
while True:
    i = int(input('Mostrar notas de qual aluno? [999 interrompe]:'))
    if i == 999:
        break
    if i >= 0 and i < len(alunos[0]):
        print("="*30)
        print(f'Notas de {alunos[0][i]}:{alunos[1][i]}.')
        print("="*30)
    else:
        print('Aluno não encontrado!Tente novamente!')
print('Fim do programa, obrigado por usar nosso sistema!')
