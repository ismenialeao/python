# ALUGUEL DE CARROS

# Qti km percorrido por um carro alugado que custa R$60 dia e R$0,15 por km

dias =  int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados? '))
pago = dias * 60
print('O total a pagar é de R${:.2f}' .format(pago))