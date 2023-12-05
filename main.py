import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.mixer.init()

LARGURA = 600
ALTURA = 600

screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Nome do jogo") # Vamos decidir

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()