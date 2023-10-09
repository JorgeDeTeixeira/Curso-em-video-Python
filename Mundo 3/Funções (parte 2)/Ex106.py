def ajuda_com_cores(comando):
    """
    Função que exibe o help do comando com cores.
    """
    cores = {
        'limpa': '\033[m',
        'azul': '\033[34m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'roxo': '\033[35m',
        'ciano': '\033[36m',
        'negrito': '\033[1m',
        'fundo_azul': '\033[44m',
        'fundo_verde': '\033[42m',
    }
    titulo = f"Acessando o manual do comando '{comando}'"
    print(f"{cores['fundo_azul']}{cores['negrito']}~" * len(titulo))
    print(titulo)
    print("~" * len(titulo))
    print(f"{cores['limpa']}", end="")
    help(comando)


while True:
    comando = input("Digite um comando (ou 'FIM' para sair): ").strip().lower()
    if comando == 'fim':
        print("Até logo!")
        break
    ajuda_com_cores(comando)
