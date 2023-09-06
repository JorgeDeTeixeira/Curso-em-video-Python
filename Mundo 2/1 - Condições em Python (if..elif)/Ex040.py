# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
n1 = float(input('Informe a primeira nota:'))
n2 = float(input('Informe a segunda nota:'))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'com média {media:.1f} sua situação é Reprovado!')
elif media >= 5.0 and media < 7:
    print(f'Com média {media:.1f} sua situação é Recuperação! ')
elif media >= 7.0 and media <= 10.0:
    print(f'Com média {media:.1f} sua situação é Aprovado!')
else:
    print('Média invalida!')
