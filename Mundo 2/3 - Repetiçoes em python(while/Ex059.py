# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
print('MENU DE MATEMÁTICA')
n1 = float(input('Primeiro valor:'))
n2 = float(input('Segundo valor:'))
sair = False
while not sair:
    print('='*20)
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opc = int(input('Sua opção:'))
    if opc == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opc == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opc == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
        else:
            print('Os dois são iguais!')
    elif opc == 4:
        print('Informe os números novamente!')
        n1 = float(input('Primeiro valor:'))
        n2 = float(input('Segundo valor:'))
    elif opc == 5:
        print('Obrigado por usar nosso sistema!')
        sair = True

    else:
        print('Opção invalida!')
