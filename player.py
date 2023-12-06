"""
Módulo contendo a definição das classes Ship, responsável pela nave controlada
pelo jogador, e Shot, referente aos tiros gerados pela nave.
"""

import pygame
from screens import LARGURA, ALTURA
import sprites as spr
import math

# Classe da nave do player
class Ship(pygame.sprite.Sprite):
    """
    Classe da nave controlada pelo jogador.

    :ivar image: Imagem do objeto.
    :ivar rect: Retângulo utilizado para orientar a imagem.
    :ivar x: Coordenada x do objeto.
    :ivar y: Coordenada y do objeto.
    :ivar speed: Velocidade do objeto.
    """
    def __init__(self):
        """
        Construtor da classe Ship.
        """
        pygame.sprite.Sprite.__init__(self)
        # Imagem da nave
        self.image = spr.img_ship
        self.rect = self.image.get_rect()
        # Coordenadas da nave
        self.x = LARGURA/2
        self.y = ALTURA/2
        self.rect.center = (self.x, self.y)
        # Velocidade da nave
        self.speed = 5

    # Método para movimentar a nave
    def move(self, direction):
        """
        Método que movimenta a nave de acordo com o pressionamento das teclas WASD.

        :param direction: Indica a direção para a qual o movimento ocorrerá.
        :type direction: str
        """
        # Para cima, baixo, esquerda e direita
        if direction == "up" and self.y > 0 + self.rect.height/2:
            self.y = self.y - self.speed
        elif direction == "down" and self.y < ALTURA - self.rect.height/2:
            self.y = self.y + self.speed
        elif direction == "left" and self.x > 0 + self.rect.width/2:
            self.x = self.x - self.speed
        elif direction == "right" and self.x < LARGURA - self.rect.width/2:
            self.x = self.x + self.speed
        # Nas diagonais, a velocidade é dividida por raiz de 2 para manter a 
        # velocidade de movimento constante
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

    # Método padrão para atualizar as coordenadas da imagem
    def update(self):
        """
        Atualizador da sprite da classe Ship.
        """
        self.rect.center = (self.x, self.y)


# Classe dos tiros do player
class Shot(pygame.sprite.Sprite):
    """
    Classe dos tiros gerados pela nave.

    :ivar image: Imagem do objeto.
    :ivar rect: Retângulo utilizado para orientar a imagem.
    :ivar x: Coordenada x do objeto.
    :ivar y: Coordenada y do objeto.
    :ivar speed: Velocidade do objeto.
    """
    def __init__(self, x, y):
        """
        Inicializador do objeto.

        :param x: Coordenada x de surgimento do objeto.
        :type x: int
        :param y: Coordenada y de surgimento do objeto.
        :type y: int
        """
        pygame.sprite.Sprite.__init__(self)
        # Imagem do tiro
        self.image = spr.img_shot
        # Coordenadas do tiro
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        # Velocidade do tiro
        self.speed = 10

    # Método para movimentar o tiro
    def move(self):
        """
        Método que movimenta o tiro para cima.
        """
        self.y = self.y - self.speed

    # Método para atualizar a posição da imagem do tiro
    def update(self):
        """
        Atualizador da sprite da classe Ship.
        """
        # O "move" foi chamado aqui por praticidade, já que o update já seria chamado de qualquer forma
        self.move()
        self.rect.center = (self.x, self.y)