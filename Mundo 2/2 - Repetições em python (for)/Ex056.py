# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idades = 0
maiorIdade = 0
homemVelho = ''
mulheres20 = 0
for p in range(1, 5):
    print(f'---{p}° pessoa.---')
    nome = str(input('Nome:')).strip().capitalize()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper().strip()[0]
    idades += idade
    if p == 1 and sexo == 'M':
        maiorIdade = idade
        homemVelho = nome
    else:
        if idade > maiorIdade and sexo == 'M':
            maiorIdade = idade
            homemVelho = nome
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
media = idades / 4
print(F'A media de idade do grupo é:{media:.2f}.')
print(f'O homem mais velho se chama {homemVelho} e tem {maiorIdade} anos.')
print(f'Tem um total de {mulheres20} mulheres com menos de 20 anos.')
