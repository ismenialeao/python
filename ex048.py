# soma multiplos de tres entre 1 a 500

s = 0
for c in range(1, 501, 2):        # vai de 1 a 500 pulando de 2 em 2
    if c %3 == 0:            #multiplo de 3
    s = s + c
    print('A soma de todos valores é {}' .format(s))

#voltar aqui
