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
        """
        Propriedade do atributo atual.
        """
        return self.__atual
    
    @property
    def image(self):
        """
        Propriedade do atributo image.
        """
        return self.__image
    
    @property
    def list_images(self):
        """
        Propriedade do atributo list_images.
        """
        return self.__list_images
    
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
    def rect(self):
        """
        Propriedade do atributo rect.
        """
        return self.__rect
    
    @property
    def x_speed(self):
        """
        Propriedade do atributo x_speed.
        """
        return self.__x_speed
    
    @property
    def y_speed(self):
        """
        Propriedade do atributo y_speed.
        """
        return self.__y_speed
    
    @atual.setter
    def atual(self, new_atual):
        """
        Setter do atributo atual.

        :param new_atual: tempo atual.
        :type new_atual: int.
        """
        self.__atual = new_atual

    @image.setter
    def image(self, new_image):
        """
        Setter do atributo image.

        :param new_image: nova imagem alterada.
        :type new_atual: int.
        """
        self.__image = new_image

    @x.setter
    def x(self, new_x):
        """
        Setter do atributo x.

        :param new_x: nova coordenada eixo x.
        :type new_x: int.
        """
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        """
        Setter do atributo y.

        :param new_y: nova coordenada eixo y.
        :type new_y: int.
        """
        self.__y = new_y

    @x_speed.setter
    def x_speed(self, new_x_speed):
        """
        Setter do atributo x_speed.

        :param new_x_speed: nova velocidade no eixo x.
        :type new_x_speed: int.
        """
        self.__x_speed = new_x_speed

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

    """
#Redefinindo o movimento do cometa
    def _move(self):
        """
        Método que movimenta o objeto espacial.
        Herdado da classe base Space Object. 
        """
        # Reposiciona o cometa acima da tela em uma posição aleatória
        if self.y > ALTURA + 100:
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


    

  



    