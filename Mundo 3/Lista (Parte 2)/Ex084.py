# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dados = list()
pessoas = list()
maiorP = list()
menorP = list()
while True:
    dados.append(str(input("Nome:")).strip())
    dados.append(float(input('Peso:')))
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    if resp == 'N':
        break
maior = menor = 0
for p in range(0, len(pessoas)):
    print(pessoas[p])
    if p == 0:
        maior = menor = pessoas[0][1]
    else:
        if pessoas[p][1] > maior:
            maior = pessoas[p][1]

        if pessoas[p][1] < menor:
            menor = pessoas[p][1]
for pos, p in enumerate(pessoas):
    if maior == p[1]:
        maiorP.append(p[0])
    if menor == p[1]:
        menorP.append(p[0])
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}.Peso de {maiorP}')
print(f'O menor peso foi de {menor}.Peso de {menorP}')
