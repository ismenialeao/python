# numeros primos

num = int(input('Digite um numero:'))

for c in range(1, num + 1):
    if num % c == 0:          # se o numero for divisivel fica amarelo
        print('\033[33m', end='') # isso muda a cor
    else:
        print('\033[31m', end='')   #se não fica vermelho
    print('{}' .format(c) , end= '')