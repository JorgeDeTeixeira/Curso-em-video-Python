def aumentar(valor=0, por=0):
    res = valor + (valor * por / 100)
    return res


def diminuir(valor=0, por=0):
    res = valor - (valor * por / 100)
    return res


def dobro(valor=0):
    res = valor * 2
    return res


def metade(valor=0):
    res = valor / 2
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:8.2f}'.replace('.', ',')


def title(tam=0, txt=''):
    print(f'=' * tam)
    print(f'{txt.center(tam)}')
    print(f'=' * tam)


def resumo(valor=0, aum=10, dim=5):
    title(30, 'RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{moeda(dobro(valor))}')
    print(f'Metade do preço: \t{moeda(metade(valor))}')
    print(f'{aum}% de aumento: \t{moeda(aumentar(valor, aum))}')
    print(f'{dim}% de redução: \t{moeda(diminuir(valor, dim))}')


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: "{entrada}" é um preço inválido!')
        else:
            valido = True
            return float(entrada)
