"""
Módulo para definição das classes Ufo e Laser, são os inimigos automáticos do jogador,
ambos causam dano ao jogador se colidirem 
"""
import pygame
from screens import LARGURA, ALTURA
import sprites as spr
from random import randint

# Definindo uma classes para o objeto ovni
class Ufo(pygame.sprite.Sprite):
    """
    Classe Ufo, nave que passa aleatoriamente pela tela e aciona lasers

    :ivar __image_ufo: Lista de imagens para criar a rotação
    :ivar __index_lista: Variável para alternar entre as imagens da lista
    :ivar __image: imagem atual da tela
    :ivar __rect: Retângulo ao redor da imagem
    :ivar __direction: Variável que define se o objeto está acima ou no meio da tela (gerada aleatoriamente)
    :ivar __shoot: Variável para armazenar se o objeto pode acionar o laser
    """
    def __init__(self):
        """
        Inicializador da classe Ufo
        """
        pygame.sprite.Sprite.__init__(self)
        # Adicionando a imagem 
        self.__image_ufo = spr.list_images_ufo

        # Uma variável para alternar entre as imagens 
        self.__index_list = 0
        self.__image = self.image_ufo[self.index_list]

        self.__rect = self.image.get_rect()
        
        # Definindo onde vai ser a primeira geração do objeto
        self.rect.x = - LARGURA
        
        # Sorteando a posição y
        self.__direction = randint(0,1)

        self.__shoot = 0

    # Prpriedades do objeto
    @property
    def shoot(self):
        """
        Propriedade do atributo shoot
        """
        return self.__shoot
    
    @property
    def rect(self):
        """
        Propriedade do atributo rect
        """
        return self.__rect
    
    @property
    def image(self):
        """
        Propriedade do atributo image
        """
        return self.__image
    
    @property
    def direction(self):
        """
        Propriedade do atributo direction
        """
        return self.__direction
    
    @property
    def index_list(self):
        """
        Propriedae do atributo index_list
        """
        return self.__index_list
    
    @property
    def image_ufo(self):
        """
        Propriedade do atributo image_ufo
        """
        return self.__image_ufo
    
    # Setter dos atributos
    @shoot.setter
    def shoot(self, new_shoot):
        """
        Setter para o atributo shoot

        :param new_shoot: novo estado
        :type new_shoot: int
        """
        self.__shoot = new_shoot

    @index_list.setter
    def index_list(self, new_index):
        """
        Setter do atributo index_list

        :param new_index: novo index para lista de imagens
        :type new_index: float
        """
        self.__index_list = new_index

    @image.setter
    def image(self, new_image):
        """
        Setter para o atributo image

        :param new_image: nova imagem
        :type new_image: pygame.surface.Surface
        """
        self.__image = new_image

    @direction.setter
    def direction(self, new_direction):
        """
        Setter do atributo direction

        :param new_direction: nova direção da nave
        :type new_direction: int
        """
        self.__direction = new_direction

    def __move(self):
        """
        Método para definir o movimento do objeto pela tela e ciclo do ressurgimento
        """
        # Movimentação pelo eixo x
        self.rect.x += 1

        # Definindo a posição y
        if self.direction == 0:
            self.rect.y = 50

        if self.direction == 1:
            self.rect.y = ALTURA//2       

        # Definindo o ciclo de ressurgimento
        if self.rect.x > 2*LARGURA:
            self.rect.x = - LARGURA
            # Sorteando a posição do y
            self.direction = randint(0,1)

    def update(self):
        """
        Método para atualizar a imagem, movimento e outras variáveis do objeto
        """
        # Alternando entre as imagens 
        if self.index_list > 24:
            self.index_list = 0
        self.index_list += 0.25
        self.image = self.image_ufo[int(self.index_list)]

        # Mover a nave pelo eixo x
        self.__move()

        # Se a nave  estiver na tela a variável será verdadeira
        if self.rect.x > 10 and self.rect.x < LARGURA:
            self.shoot = 1
        else:
            self.shoot = 0


# Definindo a classe que será o tiro do ovni
class Laser(pygame.sprite.Sprite):
    """
    Classe dos Lasers acionados pelo ovni

    :ivar __image: imagem do laser
    :ivar __alien: objeto que aciona o laser
    :ivar __rect: Retângulo ao redor da imagem
    """
    def __init__(self, alien):
        """
        Inicializador da classe

        :param alien: Objeto que dispara o laser
        :type alien: ufo.Ufo
        """
        pygame.sprite.Sprite.__init__(self)
        # Adicionando imagem
        self.__image = spr.img_laser
        # Adicionando qual será o objeto que disparará o tiro
        self.__alien = alien

        # Adiconando as posições do tiro, a partir do alien
        self.__rect = self.image.get_rect()
        self.rect.center = (self.alien.rect.center[0], self.alien.rect.center[1] + 20)
    
    # Propriedades do objeto
    @property
    def rect(self):
        """
        Propriedade do atributo rect
        """
        return self.__rect
    
    @property
    def image(self):
        """
        Propriedade do atributo image
        """
        return self.__image
    
    @property
    def alien(self):
        """
        Propriedade do atributo alien
        """
        return self.__alien
    
    def __move(self):
        """
        Método para movimentação do laser pela tela
        """
        # O laser será acionando se o alien estiver acima da tela
        if self.alien.direction == 0:
            self.rect.y += 2

    def update(self):
        """
        Método para atualizar o movimento do objeto
        """
        # Atualizando as imagens e movimento
        self.__move()