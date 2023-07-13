largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))

area = largura * altura

print(
    f'Para pintar uma parede com {largura}m2 de largura e {altura}m2 de altura com uma área de {area}m2.')
print(f'É necessário {area / 2}L de tinta.')
