def linha(tam=40):
    return '=' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40).upper())
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mErro: por favor, digite um número inteiro válido.\033[m')
        else:
            return n


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for c, i in enumerate(lista):
        print(f'\033[33m{c + 1}\033[m - \033[34m{i}\033[m')
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m')
    return opc