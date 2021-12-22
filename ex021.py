#Tocando um mp3 , musica

 import pygame
 pygame.init()
 pygame.mixer.music.load('ex21.mp3 ')
 pygame.mixer.music.play()
 pygame.event.wait()