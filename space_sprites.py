"""
Módulo contendo a definição da classe SpaceSprites, responsável pelo background
do jogo. Ela é invocada no módulo "sprites".
"""

import pygame

# Classe das imagens de fundo
class SpaceSprites(pygame.sprite.Sprite):
    """
    Classe referente ao background do jogo.

    :ivar __image: Imagem de fundo.
    :ivar __rect: Retângulo utilizado para orientar a imagem.
    :ivar __x: Coordenada x da imagem.
    :ivar __y: Coordenada y da imagem.
    :ivar __speed: Velocidade de movimento da imagem.
    """
    def __init__(self, x, y, image):
        """
        Inicializador do objeto.

        :param __x: Coordenada x inicial da imagem.
        :type __x: int
        :param __y: Coordenada y inicial da imagem.
        :type __y: int
        :param __image: Caminho da imagem a ser carregada.
        :type __image: str
        """
        pygame.sprite.Sprite.__init__(self)
        # Imagens do objeto
        self.__image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (600, 600))
        # Coordenadas das imagens
        self.__x = x
        self.__y = y
        self.__rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.__speed = 1

    # Getters para os atributos da classe
    @property
    def image(self):
        """
        Propriedade do atributo image.
        """
        return self.__image
    
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
    def speed(self):
        """
        Propriedade do atributo speed.
        """
        return self.__speed
    
    # Setters necessários para os atributos da classe
    @image.setter
    def image(self, new_image):
        """
        Setter do atributo image.

        :param new_image: Nova imagem.
        :type new_image: int
        """
        self.__image = new_image

    @y.setter
    def y(self, new_y):
        """
        Setter do atributo y.

        :param new_y: Nova coordenada y.
        :type new_y: int
        """
        self.__y = new_y

    # Método para movimentar as imagens de fundo
    def update(self):
        """
        Atualizador da sprite, que se movimenta continuamente para baixo.
        """
        self.y = self.y + self.speed
        self.rect.topleft = (self.x, self.y)
        # A imagem volta para cima quando sai da tela por baixo
        if self.y > 600:
            self.y = -600