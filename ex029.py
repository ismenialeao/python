# Par ou impar

numero = int(input('Me diga um numero: '))
resultado = numero % 2
print('O resultado foi {}' .format(resultado))
if resultado == 0:
    print('seu numero {} é par'.format(numero))
else:
    print('Seu numero {} é impar'.format(numero))