string = 'Jorge Teixeira'

# Fatiamento
print('Fatiamento'.upper())
print(f'Do espaço 0 ao 1:{string[0:3]}')  # Do espaço 0 ao 2
# Do espaço 0 ao 4 pulando de 2 em dois
print(f'Do espaço 0 ao 4 pulando de 2 em dois:{string[0:5:2]}')
# Omitindo o inicio, mesma coisa que do inicio ate o espaço 5
print(
    f'Omitindo o inicio, mesma coisa que do inicio ate o espaço 5:{string[:5]}')
# Idicando o inicio, mesma coisa que do inicio ate o final da string
print(
    f'Idicando o inicio, mesma coisa que do inicio ate o final da string:{string[1:]}')
print(f'Do 0 até o final pulando de 2 em 2:{string[0::2]}')

print('\n')
print(f"Analisando a palavra {string}.")
# Analise
print(f'Tamanho da frase:{len(string)}')  # Len comprimento
print(f'Quantas letras o:{string.count("o")}') # Count Contar quantas letras tem na frase () string.count("o", 0, 5) = Já usando o fatiamento}
print(f'A palvra começa a partir do momento:{string.find("rge")}') #Find procura apartir de qual posição começa a palavra que quer achar
print(f'{string.find("Clara")}') #-1 significa que não achou
print(f'') #Operador in returno true ou false

print('\n')
print('tranformação.'.upper())

print(string.replace('Teixeira', 'Melo')) #Replace trocar a palavra
print(string.upper()) #Em maiusculo
print(string.lower()) #Em minusculo
print(string.capitalize()) #Só a primeira letra fica maiusculo
print(string.title()) #Deixa todas as primeiras letras das frases em maiusculo
print(string.strip()) ##Remove todos os espaços desnecessarios no final e no inicio
print(string.rstrip()) ##Remove apenas os espaços do final
print(string.lstrip()) ##Remove apenas os espaços do inicio

print('\n')
print('DIVISÃO')

print(string.split()) #Split divide uma string em uma lista pelos espaços

print('\n')
print('JUNÇÃO')

print(' '.join(string))#Join separa a string em qualquer caractere

print('\n')
print('PRATICA')
