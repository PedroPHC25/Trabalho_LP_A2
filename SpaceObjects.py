"""
Módulo contendo a definição das classes SpaceObject, que é pai das classes BigMeteor e comet, que é responsável pelos objestos espaciais 
que causam dano na nave, como meteoros e cometas.
"""
import pygame
from abc import ABC, abstractmethod
from random import randrange
from screens import ALTURA, LARGURA

# Classe abstrata que define o que todo objeto espacial deve ter
class SpaceObject(ABC, pygame.sprite.Sprite):
    """
    Classe de objeto espacial, que causa dano na nave.

    :ivar __image: Imagem do objeto.
    :ivar __rect: Retângulo utilizado para orientar a imagem.
    :ivar __x: Coordenada x do objeto.
    :ivar __y: Coordenada y do objeto.
    :ivar __speed: Velocidade do objeto.
    :ivar __atual: Estado atual que definea mudança dos sprites e começa em zero.
    """
    #Inicializador do objeto e definições dos sprites
    def __init__(self, y, list_images):
        """
        Construtor da classe SpaceObject.

        :param y: Posição inicial do objeto na tela no eixo y.
        :type y: int
        :param list_images: Lista contendo as imagens dos sprites do objeto espacial.
        :type list_images: list
        """
        pygame.sprite.Sprite.__init__(self)
        # Posição inicial do objeto, aleatória no eixo x
        self.__x = randrange(50, 550, 10)
        self.__y = y
        
        # Imagem inicial que define o sprite e altera com o tempo
        self.__atual= 0
        self.__list_images = list_images
        self.__image = list_images[self.atual]
        self.__rect = self.image.get_rect()
        self.rect.center = (self.x, self.y) 
        # Velocidade do objeto
        self.__x_speed = 3 
        self.__y_speed = 3

    @property
    def atual(self):
        return self.__atual
    
    @property
    def image(self):
        return self.__image
    
    @property
    def list_images(self):
        return self.__list_images
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def x_speed(self):
        return self.__x_speed
    
    @atual.setter
    def atual(self, new_atual):
        self.__atual = new_atual

    @image.setter
    def image(self, new_image):
        self.__image = new_image

    @image.setter
    def x(self, new_x):
        self.__x = new_x

    @image.setter
    def y(self, new_y):
        self.__y = new_y

    # Método abstrato que define a movimentação do objeto    
    @abstractmethod
    def _move(self):
        """
        Método abstrato que movimenta o objeto espacial de acordo com o seu tipo.
        Será herdado e definido na classe filha.
        """
        ...
    
    # Método que atualiza a posição do objeto e define a troca de imagem do sprite
    def update(self):
        """
        Atualizador da sprite da classe SpaceObject.
        """
        # Muda o estado de acordo com o tempo, para a atualização da sprite.
        self.atual = self.atual + 0.3
        if self.atual >= len(self.list_images):
            self.atual = 0

        self.image = self.list_images[int(self.atual)]
        self.rect.center = (self.x, self.y)
        self._move()




# Classe que herda de SpaceObject e cria o objeto meteoro grande
class BigMeteor(SpaceObject):
    """
    Classe referente ao  objeto BigMeteor, que herda de SpaceObject.

    """
    # Redefinição do método abstrato que controla a movimentação
    def _move(self):
        """
        Método que movimenta o objeto espacial.
        Herdado da classe base SpaceObject.
        """
        # Condicional que define o resurgimento da sprite no game loop, de maneira aleatória. 
        if self.y > ALTURA + 100:
            self.y = randrange(-600, -200)
            self.x = randrange(50, 550)

        # Alteração da posição do meteoro de acordo com a velocidade herdada de SpaceObject.
        self.x += self.x_speed 
        self.y += self.y_speed

        # Condicional que define o a colisão do meteoro com a tela lateral e rebote.
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


    

  



    