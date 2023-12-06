"""
Módulo contendo a definição das classes SpaceObject, que é pai das classes BigMeteor e --------, que é responsável pelos objestos espaciais 
que causam dano na nave, como meteoros e cometas.
"""
import pygame
from abc import ABC, abstractmethod
from random import randrange
from screens import ALTURA, LARGURA

# Classe abstrata que define o que todo objeto espacial deve ter
class SpaceObject(ABC, pygame.sprite.Sprite):
    #Inicializador do objeto e definições dos sprites
    def __init__(self, y, list_images):
        pygame.sprite.Sprite.__init__(self)
        self.x = randrange(50, 550, 10)
        self.y = y
        self.atual= 0
        self.list_images = list_images
        self.image = list_images[self.atual]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y) 
        self.x_speed = 3 
        self.y_speed = 3

    # Método abstrato que define a movimentação do objeto    
    @abstractmethod
    def _move(self): ...
    
    # Método que atualiza a posição do objeto e define a troca de imagem do sprite
    def update(self):
        self.atual = self.atual + 0.3
        if self.atual >= len(self.list_images):
            self.atual = 0

        self.image = self.list_images[int(self.atual)]
        self.rect.center = (self.x, self.y)
        self._move()

# Classe que herda de SpaceObject e cria o objeto meteoro grande
class BigMeteor(SpaceObject):
    # Redefinição do método abstrato que controla a movimentação
    def _move(self):
        if self.y > ALTURA + 100:
            self.y = randrange(-600, -200)
            self.x = randrange(50, 550)
        self.x += self.x_speed 
        self.y += self.y_speed

        if self.x > LARGURA-(20) or self.x < (20):
            self.x_speed = self.x_speed * (-1)

# Classe que herda de SpaceObject e cria o objeto cometa verde
class Comet(SpaceObject):

    # Redefinição do método abstrato que controla a movimentação
    def _move(self):
        if self.y > ALTURA + 100:
            self.y = randrange(-600, -200)
            self.x = randrange(0, 550)
        self.x_speed = 0 
        self.y += self.y_speed

        if self.x > LARGURA-(20) or self.x < (20):
            self.x_speed = self.x_speed * (-1)



    

  



    