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

# Classe que herda de SpaceObject e cria o objeto cometa 
class Comet(SpaceObject):
    """
    Classe que representa um cometa no jogo, derivada da classe SpaceObject.

    Métodos:
    - _move(): Método responsável por controlar a movimentação do cometa.
    """

    def _move(self):
        """
        Redefine o método abstrato _move() da classe pai SpaceObject.

        Regras de movimentação do cometa:
        1. Se a posição y do cometa for maior que ALTURA + 100,
           reposiciona o cometa acima da tela em uma posição aleatória.
        2. Define a velocidade horizontal (x_speed) do cometa como 0.
        3. Atualiza a posição y do cometa baseada na sua velocidade vertical (y_speed).
        4. Se a posição x do cometa ultrapassar os limites da tela,
           inverte a direção do movimento horizontal multiplicando x_speed por -1.
        """
        if self.y > ALTURA + 100:
            # Reposiciona o cometa acima da tela em uma posição aleatória
            self.y = randrange(-600, -200)
            self.x = randrange(0, 550)

        # Define a velocidade horizontal como 0
        self.x_speed = 0

        # Atualiza a posição vertical do cometa
        self.y += self.y_speed

        # Verifica se o cometa ultrapassou os limites horizontais da tela
        if self.x > LARGURA - 20 or self.x < 20:
            # Inverte a direção do movimento horizontal
            self.x_speed = self.x_speed * (-1)


    

  



    