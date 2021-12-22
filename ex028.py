# jogo de adivinha

from random import randint
Computador = randint(0, 5)
print('===='*15)
print('Pense em um numero de 0 a 5')
jogador = int(input('Em que numero eu pensei? '))

if jogador == computador:

    print('Parabens. Vc venceu')
else: print('Ganhei pensei no numero {}' .format(computador , jogador))