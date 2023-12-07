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

    :ivar __image: Imagem do objeto.
    :ivar __rect: Retângulo utilizado para orientar a imagem.
    :ivar __x: Coordenada x do objeto.
    :ivar __y: Coordenada y do objeto.
    :ivar __speed: Velocidade do objeto.
    """
    def __init__(self):
        """
        Construtor da classe Ship.
        """
        pygame.sprite.Sprite.__init__(self)
        # Imagem da nave
        self.__image = spr.img_ship
        self.__rect = self.image.get_rect()
        # Coordenadas da nave
        self.__x = LARGURA/2
        self.__y = 400
        self.rect.center = (self.x, self.y)
        # Velocidade da nave
        self.__speed = 5
        # Vida da nave
        self.__health = 5

    # Propriedades para os atributos da classe
    @property
    def x(self):
        """
        Propriedade do atributo x.
        """
        return self.__x
    
    @property
    def y(self):
        """
        Propriedade do atributo y.
        """
        return self.__y
    
    @property
    def image(self):
        """
        Propriedade do atributo image.
        """
        return self.__image
    
    @property
    def rect(self):
        """
        Propriedade do atributo rect.
        """
        return self.__rect
    
    @property
    def speed(self):
        """
        Propriedade do atributo speed.
        """
        return self.__speed
    
    @property
    def health(self):
        """
        Propriedade do atributo health.
        """
        return self.__health
    
    # Setters dos atributos necessários
    @x.setter
    def x(self, new_x):
        """
        Setter do atributo x.

        :param new_x: Nova coordenada x.
        :type new_x: int
        """
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        """
        Setter do atributo y.

        :param new_y: Nova coordenada y.
        :type new_y: int
        """
        self.__y = new_y

    @health.setter
    def health(self, new_health):
        """
        Setter do atributo health.

        :param new_health: Nova vida.
        :type new_health: int
        """
        self.__health = new_health

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

    # Método para fazer a nave tomar dano
    def take_damage(self):
        """
        Método para dar dano na nave.
        """
        self.health -= 1

    # Método para fazer a nave tomar dano
    def increase_health(self):
        """
        Método para dar vida para a nave.
        """
        if self.health < 5:
            self.health += 1

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

    :ivar __image: Imagem do objeto.
    :ivar __rect: Retângulo utilizado para orientar a imagem.
    :ivar __x: Coordenada x do objeto.
    :ivar __y: Coordenada y do objeto.
    :ivar __speed: Velocidade do objeto.
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
        self.__image = spr.img_shot
        # Coordenadas do tiro
        self.__x = x
        self.__y = y
        self.__rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        # Velocidade do tiro
        self.__speed = 10

    # Propriedades para os atributos da classe.
    @property
    def x(self):
        """
        Propriedade do atributo x.
        """
        return self.__x

    @property
    def y(self):
        """
        Propriedade do atributo y.
        """
        return self.__y
    
    @property
    def image(self):
        """
        Propriedade do atributo image.
        """
        return self.__image
    
    @property
    def rect(self):
        """
        Propriedade do atributo rect.
        """
        return self.__rect

    @property
    def speed(self):
        """
        Propriedade do atributo speed.
        """
        return self.__speed
    
    # Setter necessário para o atributo y.
    @y.setter
    def y(self, new_y):
        """
        Setter do atributo y.

        :param new_y: Nova coordenada y.
        :type new_y: int
        """
        self.__y = new_y

    # Método para movimentar o tiro
    def move(self):
        """
        Método que movimenta o tiro para cima.
        """
        self.y = self.y - self.speed
        # Destrói o objeto assim que ele sai da tela
        if self.y < 0:
            self.kill()

    # Método para atualizar a posição da imagem do tiro
    def update(self):
        """
        Atualizador da sprite da classe Ship.
        """
        # O "move" foi chamado aqui por praticidade, já que o update já seria chamado de qualquer forma
        self.move()
        self.rect.center = (self.x, self.y)