nome = str(input('Nome:'))
if nome == 'Gustavo':
    print('Nome bonito')
elif nome == 'Pedro' or nome == 'Maria':
    print('Nome popular')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Nome normal')