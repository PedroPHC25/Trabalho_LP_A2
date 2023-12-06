import pygame
from screens import LARGURA, ALTURA
from random import randrange
from screens import LARGURA, ALTURA
import sprites as spr
from pygame.locals import QUIT

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ufo = spr.list_images_ufo

        self.index_lista = 0
        self.image = self.image_ufo[self.index_lista]

        self.rect = self.image.get_rect()

        self.rect.center = (LARGURA//2, ALTURA//2)

    def update(self):
        if self.index_lista > 24:
            self.index_lista = 0
        self.index_lista += 0.02
        self.image = self.image_ufo[int(self.index_lista)]

ufo = Alien()
todas_sprites = pygame.sprite.Group()
todas_sprites.add(ufo)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))

while True:
    tela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    todas_sprites.draw(tela)
    todas_sprites.update()


    pygame.display.flip()

    