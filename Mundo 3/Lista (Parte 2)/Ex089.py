alunos = [[], [], []]

while True:
    # Solicita o nome do aluno
    alunos[0].append(str(input('Nome: ')))

    notas = []

    # Solicita as notas do aluno e verifica a validade
    for c in range(1, 3):
        while True:
            try:
                nota = float(input(f'Nota {c}°: '))
                if 0 <= nota <= 10:
                    break
                else:
                    print("Nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Digite uma nota válida.")

        notas.append(nota)

    # Armazena as notas e calcula a média
    alunos[1].append(notas[:])
    media = sum(notas) / 2
    alunos[2].append(media)

    notas.clear()

    resp = ' '

    # Verifica se o usuário deseja continuar
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if resp == 'N':
        break

print('=' * 30)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print("=" * 30)

# Exibe os resultados formatados
for p in range(len(alunos[0])):
    print(f'{p:<4} {alunos[0][p]:<10} {alunos[2][p]:>8.2f}')
print("=" * 30)

while True:
    i = int(input('Mostrar notas de qual aluno? [999 interrompe]:'))
    if i == 999:
        break
    if 0 <= i < len(alunos[0]):
        print("=" * 30)
        print(f'Notas de {alunos[0][i]}: {alunos[1][i]}')
        print("=" * 30)
    else:
        print('Aluno não encontrado! Tente novamente!')
        
print('Fim do programa, obrigado por usar nosso sistema!')
