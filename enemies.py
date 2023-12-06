import pygame
from abc import ABC, abstractmethod
from screens import LARGURA, ALTURA
from random import randrange
from sprites import list_images_big_meteor

class Enemy(ABC, pygame.sprite.Sprite):
    def __init__(self, y, list_images):
        pygame.sprite.Sprite.__init__(self)
        self.x = randrange(50, 550, 10)
        self.y = y
        self.list_images = list_images
        self.image = list_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    @abstractmethod
    def _move(self): ...


class BigMeteor(Enemy):
    def _move(self):
        if self.y > 600:
            self.y = 0
        self.x += 10
        self.y += 10

    def update(self):
        self.rect.center = (self.x, self.y)
        self._move()




    