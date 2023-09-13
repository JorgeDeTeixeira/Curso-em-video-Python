# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
mais18 = homens = mulheresMenos20 = 0
while True:
    print('='*20)
    print('CADASTRO DE PESSOAS')
    print('='*20)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Quantas pessoas tem mais de 18 anos:{mais18}')
print(f'Quantos homens foram cadastrados:{homens}')
print(f'Quantas mulheres tem menos de 20 anos:{mulheresMenos20}')
