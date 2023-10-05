# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.
def area(comprimento, largura):
    area = comprimento * largura
    print(
        f'A área de comprimento de {comprimento} x {largura} é igual a {area}m°.')


print('='*30)
print(f'{"CONTROLE DE TERRENOS":^30}')
print('='*30)

comprimento = float(input('Informa a comprimento do terrero:'))
largura = float(input('Informa o largura do terrero:'))
area(comprimento, largura)
