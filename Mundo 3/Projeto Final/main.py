from projeto.lib.interface import *
from projeto.lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                    'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        # Listar o conteudo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('novo cadastro')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo.')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
