import pygame
from pygame.locals import *
from sys import exit
from screens import screen, LARGURA, ALTURA
from player import Ship

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

ship = Ship()
all_sprites.add(ship)

while True:
    clock.tick(30)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    all_sprites.draw(screen)

    pygame.display.flip()