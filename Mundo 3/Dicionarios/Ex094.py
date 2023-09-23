# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoas = list()
mulheres = list()
acimaMedia = list()
soma = media = 0

while True:
    dado = dict()

    dado['nome'] = str(input('Nome: '))

    while True:
        dado['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if dado['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')

    dado['idade'] = int(input('Idade: '))
    soma += dado['idade']

    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if dado['sexo'] == 'F':
        mulheres.append(dado['nome'])

    pessoas.append(dado)

    if resp == 'N':
        break

print('='*30)
# A) Quantidade de pessoas cadastradas
print(f'A) Temos {len(pessoas)} pessoas cadastradas.')

media = soma / len(pessoas)
# B) Média de idade das pessoas
print(f'B) A média de idade é {media} anos.')

# C) Lista de mulheres cadastradas
print(f'C) As mulheres cadastradas foram: {", ".join(mulheres)}.')

# D) Lista de pessoas com idade acima da média
for p in pessoas:
    if p['idade'] > media:
        acimaMedia.append(p)
print('D) Lista de pessoas com idade acima da média:')
for p in acimaMedia:
    print(f'Nome: {p["nome"]}, Sexo: {p["sexo"]}, Idade: {p["idade"]}.')

print('\nENCERRADO!')
