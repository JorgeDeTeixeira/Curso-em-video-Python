# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 18:
        opc = 'NEGADO'
    elif idade > 75:
        opc = 'OPCIONAL'
    else:
        opc = 'OBRIGATÓRIO'

    return f'com {idade} anos: voto {opc}.'


ano = int(input('Em que ano você nasceu: '))
print(voto(ano))
