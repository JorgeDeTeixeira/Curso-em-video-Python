def fatorial(num, show=False):
    """
    Calcula o fatorial de um número:
    :param n: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: retorna o fatorial do número n.
    """

    from math import factorial

    if show == False:
        print(factorial(num))
    else:
        fac = 1
        while num != 0:
            print(f'{num}', end='')
            print(' x ' if num > 1 else ' = ', end='')
            fac *= num
            num -= 1
        print(fac)


help(fatorial)
fatorial(5, show=True)
