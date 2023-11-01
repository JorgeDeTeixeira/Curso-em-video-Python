# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[41mERRO: por favor digitar um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[41mERRO: por favor digitar um número real válido.\033[m')
            continue
        else:
            return n


n1 = leiaInt('Digite um inteiro:')
n2 = leiaReal('Digite um real:')
print(f'O valor digitado inteiro digitado foi {n1} e o real foi {n2}.')
