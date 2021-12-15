# CONVERSOR DE MOEDAS

# converta U$$ 1,00 = R$ 5,60

real = float(input('Quanto dinheiro vc tem na carteira ? R$? '))
dolar = real / 5.60

print('Com R${} vc pode comprar U$${:.2f}' .format(real, dolar))