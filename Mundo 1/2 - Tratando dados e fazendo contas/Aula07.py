nome = input('Qual o seu nome:')

print(f'Prazer em te conhecer {nome:20}!') #Aparecer em 20 caracteres
print(f'Prazer em te conhecer {nome:>20}!') #Aparecer em 20 caracteres #Alinhar a direita
print(f'Prazer em te conhecer {nome:<20}!') #Aparecer em 20 caracteres #Alinhar a esquerda
print(f'Prazer em te conhecer {nome:^20}!') #Aparecer em 20 caracteres #centralizar
print(f'Prazer em te conhecer {nome:=^20}!') #Aparecer em 20 caracteres #adicionar algum sinal

num = 5.6666
print(f'{num:.2f}')

print('Jorge', end=' ')#Continuar a linha = end=' '
print('Teixeira \nde melo')#quebrar a linha = \n