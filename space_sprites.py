"""
Módulo contendo a definição da classe SpaceSprites, responsável pelo background
do jogo. Ela é invocada no módulo "sprites".
"""

import pygame

# Classe das imagens de fundo
class SpaceSprites(pygame.sprite.Sprite):
    """
    Classe referente ao background do jogo.

    :ivar image: Imagem de fundo.
    :ivar rect: Retângulo utilizado para orientar a imagem.
    :ivar x: Coordenada x da imagem.
    :ivar y: Coordenada y da imagem.
    :ivar speed: Velocidade de movimento da imagem.
    """
    def __init__(self, x, y, image):
        """
        Inicializador do objeto.

        :param x: Coordenada x inicial da imagem.
        :type x: int
        :param y: Coordenada y inicial da imagem.
        :type y: int
        :param image: Caminho da imagem a ser carregada.
        :type image: str
        """
        pygame.sprite.Sprite.__init__(self)
        # Imagens do objeto
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (600, 600))
        # Coordenadas das imagens
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.speed = 1

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