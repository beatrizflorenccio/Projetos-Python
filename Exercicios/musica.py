import pygame

pygame.init()
pygame.mixer.music.load("arquivo.mp3") #coloque seu arquivo.mp3 ali
pygame.mixer.music.play()
pygame.event.wait() #espera a música encerrar para encerrar o programa
