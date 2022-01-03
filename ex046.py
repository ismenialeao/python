# contagem regressiva

for cont in range(0,11):

    print(cont)
print('Acabou')

from time import sleep
for cont2 in range(10, 0 , -1):  # de 10 a 1 soltando de um em um
    sleep(0.5)      #demora em meio segungo um numero ao outro
    print(cont2)