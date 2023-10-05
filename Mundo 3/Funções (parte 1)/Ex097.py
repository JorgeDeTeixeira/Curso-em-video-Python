# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(string):
    tam = len(string) + 8
    print('='*tam)
    print(f'    {string}')
    print('='*tam)


escreva('Jorge')
