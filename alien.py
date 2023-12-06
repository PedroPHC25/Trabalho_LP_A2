import pygame
from screens import LARGURA, ALTURA
from random import randrange
from screens import LARGURA, ALTURA
import sprites as spr
from pygame.locals import QUIT
from random import randint

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ufo = spr.list_images_ufo

        self.index_lista = 0
        self.image = self.image_ufo[self.index_lista]

        self.rect = self.image.get_rect()

        self.rect.x = -20
        self.rect.y = 10
        
        self.direcao = 0

    def update(self):
        if self.index_lista > 24:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.image_ufo[int(self.index_lista)]
        self.move()

    def move(self):
        if self.direcao == 0:
            ufo.rect.y = 10
            ufo.rect.x += 1

        if self.direcao == 1:
            ufo.rect.y = 540
            ufo.rect.x += 1        

        if ufo.rect.x > 2*LARGURA:
            ufo.rect.x = -80
            self.direcao = randint(0,1)


ufo = Alien()
todas_sprites = pygame.sprite.Group()
todas_sprites.add(ufo)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

while True:
    tela.fill((0,0,0))
    relogio.tick(90)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()        

    todas_sprites.draw(tela)
    todas_sprites.update()


    pygame.display.flip()

    