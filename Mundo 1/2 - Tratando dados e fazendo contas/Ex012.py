preco = float(input('Digite o preço do produto:'))
novoPreco = preco * 5 / 100
print(f'Com um desconto de 5% o novo preço que antes era {preco:.2f}R$ agora fica por {preco - novoPreco:.2f}R$.')