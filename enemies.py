import pygame
from abc import ABC, abstractmethod
from screens import LARGURA, ALTURA

class Enemy(ABC, pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA//2, 0)

    @abstractmethod
    def _move(self): ...


class BigMeteor(Enemy):
    def _move(self):
        if self.rect.topright > 600:
            self.rect.x = 0
        self.rect.x += 10
        self.rect.y += 10


    