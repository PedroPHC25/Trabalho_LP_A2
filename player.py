from typing import Any
import pygame
from screens import screen, LARGURA, ALTURA
import sprites as spr
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spr.img_ship
        self.rect = self.image.get_rect()
        self.x = LARGURA/2
        self.y = ALTURA/2
        self.speed = 5
        self.rect.center = (self.x, self.y)

    def move(self, direction):
        if direction == "up" and self.y > 0 + self.rect.height/2:
            self.y = self.y - self.speed
        elif direction == "down" and self.y < ALTURA - self.rect.height/2:
            self.y = self.y + self.speed
        elif direction == "left" and self.x > 0 + self.rect.width/2:
            self.x = self.x - self.speed
        elif direction == "right" and self.x < LARGURA - self.rect.width/2:
            self.x = self.x + self.speed
        elif direction == "upleft":
            if self.y > 0 + self.rect.height/2:
                self.y = self.y - self.speed/math.sqrt(2)
            if self.x > 0 + self.rect.width/2:
                self.x = self.x - self.speed/math.sqrt(2)
        elif direction == "upright":
            if self.y > 0 + self.rect.height/2:
                self.y = self.y - self.speed/math.sqrt(2)
            if self.x < LARGURA - self.rect.width/2:
                self.x = self.x + self.speed/math.sqrt(2)
        elif direction == "downleft":
            if self.y < ALTURA - self.rect.height/2:
                self.y = self.y + self.speed/math.sqrt(2)
            if self.x > 0 + self.rect.width/2:
                self.x = self.x - self.speed/math.sqrt(2)
        elif direction == "downright":
            if self.y < ALTURA - self.rect.height/2:
                self.y = self.y + self.speed/math.sqrt(2)
            if self.x < LARGURA - self.rect.width/2:
                self.x = self.x + self.speed/math.sqrt(2)

    def update(self):
        self.rect.center = (self.x, self.y)


class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = spr.img_shot
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.center = (self.x, self.y)

    def move(self):
        self.y = self.y - self.speed

    def update(self):
        self.move()
        self.rect.center = (self.x, self.y)