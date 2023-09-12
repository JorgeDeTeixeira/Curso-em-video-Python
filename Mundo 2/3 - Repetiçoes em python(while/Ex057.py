# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe o sexo [M/F]:')).strip().upper()[0]
while sexo != 'M' and sexo != 'F': #while sexo not in 'MF'
    print('Sexo inválido, tente novamente!')
    sexo = str(input('Informe o sexo [M/F]')).strip().upper()[0]
print('Sexo registrado foi com sucesso!')
