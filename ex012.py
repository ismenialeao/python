#Calculando descontos

preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto o produto ira cutar?R${:.2f}' .format(preco, novo))