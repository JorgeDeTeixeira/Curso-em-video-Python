# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

title = 'Analisador de triângulo'
print(f'{title:=^40}')

r1 = float(input('Digite o primeiro segmento de reta:'))
r2 = float(input('Digite o segundo segmento de reta:'))
r3 = float(input('Digite o terceiro segmento de reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo!')
    if r1 == r2 and r2 == r3:
        print('Triângulo EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Triângulo ESCALENO!')
    else:
        print('Triângulo ISÓSCELES!')
else:
    print('Não pode formar um triângulo!')
