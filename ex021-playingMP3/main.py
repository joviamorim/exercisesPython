import pygame

#initializing mixer
pygame.mixer.init()
# initializing pygame
pygame.init()

pygame.mixer.music.load('zeldasound.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
