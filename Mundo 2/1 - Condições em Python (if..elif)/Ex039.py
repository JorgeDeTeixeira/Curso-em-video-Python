# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

atual = date.today().year
anoNascimento = int(input('Ano de nascimento:'))
idade = atual - anoNascimento

if idade == 18:
    print('Este é o ano do seu alistamento!')
elif idade < 18:
    print(f'Ainda falta {anoNascimento + 18 - atual} para você se alistar!')
elif idade > 18:
    print(f'Passou {atual - anoNascimento - 18} anos do seu alistamento!')
