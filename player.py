import pygame
from screens import screen, LARGURA, ALTURA
import sprites as spr

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spr.img_ship
        self.rect = self.image.get_rect()
        self.x = LARGURA/2
        self.y = ALTURA/2
        self.rect.center = (self.x, self.y)