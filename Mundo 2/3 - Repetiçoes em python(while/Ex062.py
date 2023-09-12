# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('SUPER GERADOR DE PA')
print('='*20)
p1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{p1} -> ', end='')
        p1 += r
        cont += 1
    print('PAUSA')
    mais = int(input('Digite quantos termos a mais você quer ver:'))
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados!')