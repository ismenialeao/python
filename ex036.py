# Aprovando emprestimo

casa = float(input('Valor da casa R$: '))
salario = float(input('Salario do comprador: '))
anos = int(input('Anos de financiamento: '))
prestacao = casa /(anos *12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos.' .format(casa, anos), end='')
print('A prestação é de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo concedido')
else:
    print('Emprestimo Negadoooo.')