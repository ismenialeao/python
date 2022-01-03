# grupo maioridade

from datetime import date
atual = date.today().year

for pess in range(1,8):   #grupo de 8 pessoas classifica qual idade delas
    nasc = int(input('Que ano nasceu?'))
    idade = atual - nasc

    if idade >= 21:
        print('Essa pessoa é maior')

    else:
        print('Essa pessoa é menor')

    print('Esssa pessoa tem {} anos' .format(idade))

