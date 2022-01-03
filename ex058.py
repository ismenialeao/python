#JOGO DE ADIVINHAÇÃO
from random import randint #importa função sorteio aleatorio

computer = randint(0, 10)
print('Sou seu computatador... Acabei de pensar em um numero entre 0 a 10')
print('Sera que vc consegue adibinhar qual numero foi? ')
acertou = False

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    if jogador == computer:
    acertou = True

print('Acertou!')

