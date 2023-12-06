import pygame
from abc import ABC, abstractmethod
from random import randrange
from SpaceObjects import SpaceObject

# Classe que herda de SpaceObject e cria o objeto cometa verde
class greenComet(SpaceObject):
    # Redefinição do método abstrato que controla a movimentação
    def _move(self):
        if self.y > 600:
            self.y = 0
        self.x += 3
        self.y += 3