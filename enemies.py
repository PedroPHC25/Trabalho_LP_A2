import pygame
from abc import ABC, abstractmethod
from screens import LARGURA, ALTURA
from random import randrange
from sprites import list_images_big_meteor

class SpaceObject(ABC, pygame.sprite.Sprite):
    def __init__(self, y, list_images):
        pygame.sprite.Sprite.__init__(self)
        self.x = randrange(50, 550, 10)
        self.y = y
        self.atual= 0
        self.list_images = list_images
        self.image = list_images[self.atual]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y) 
        
    @abstractmethod
    def _move(self): ...
        
    def update(self):
        self.atual = self.atual + 0.5
        if self.atual >= len(self.list_images):
            self.atual = 0

        self.image = self.list_images[int(self.atual)]
        self.rect.center = (self.x, self.y)
        self._move()



class BigMeteor(SpaceObject):
    def _move(self):
        if self.y > 600:
            self.y = 0
        self.x += 5
        self.y += 5

  



    