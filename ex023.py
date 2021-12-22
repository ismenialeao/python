#separando digiros de numeros

num = int(input('Informe um numero:'))
n = str(num)
print('Analisando o numero {}'.format(num))
print('Unidade {}' .format(n[3]))
print('dezena {}' .format(n[2]))
print(('Centena {}' .format(n[1])))
print('Milhar {}'. format(n[0]))