# game de pedra , papel e tesoura

from  random import randint
itens = ('pedra, papel, tesoura')
computador = randint(0, 2)
print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [3] TESOURA''')

jogador = int(input('Qual sua jogada? '))
print(' O computador escolheu: {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))