"""
Módulo para definição das classes Ufo e Laser, são os inimigos automáticos do jogador,
ambos causam dano ao jogador se colidirem 
"""
import pygame
from screens import LARGURA, ALTURA
import sprites as spr
from random import randint
from sounds import ufo_sound

# Definindo uma classes para o objeto ovni
class Ufo(pygame.sprite.Sprite):
    """
    Classe Ufo, nave que passa aleatoriamente pela tela e aciona lasers

    :ivar __image_ufo: Lista de imagens para criar a rotação
    :ivar __index_lista: Variável para alternar entre as imagens da lista
    :ivar __image: imagem atual da tela
    :ivar __rect: Retângulo ao redor da imagem
    :ivar __direcao: Variável que define se o objeto está acima ou no meio da tela (gerada aleatoriamente)
    :ivar __atirar: Variável para armazenar se o objeto pode acionar o laser
    """
    def __init__(self):
        """
        Inicializador da classe Ufo
        """
        pygame.sprite.Sprite.__init__(self)
        # Adicionando a imagem 
        self.__image_ufo = spr.list_images_ufo

        # Uma variável para alternar entre as imagens 
        self.__index_lista = 0
        self.__image = self.image_ufo[self.index_lista]

        self.__rect = self.image.get_rect()
        
        # Definindo onde vai ser a primeira geração do objeto
        self.rect.x = - LARGURA
        self.rect.y = 50
        
        # Sorteando a posição y
        self.__direcao = randint(0,1)

        self.__atirar = 0

    # Prpriedades do objeto
    @property
    def atirar(self):
        """
        Propriedade do atributo atirar
        """
        return self.__atirar
    
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
    def direcao(self):
        """
        Propriedade do atributo direcao
        """
        return self.__direcao
    
    @property
    def index_lista(self):
        """
        Propriedae do atributo index_lista
        """
        return self.__index_lista
    
    @property
    def image_ufo(self):
        """
        Propriedade do atributo image_ufo
        """
        return self.__image_ufo
    
    # Setter dos atributos
    @atirar.setter
    def atirar(self, new_atirar):
        """
        Setter para o atributo atirar

        :param new_atirar: novo estado
        :type new_atirar: int
        """
        self.__atirar = new_atirar

    @index_lista.setter
    def index_lista(self, new_index):
        """
        Setter do atributo index_lista

        :param new_index: novo index para lista de imagens
        :type new_index: float
        """
        self.__index_lista = new_index

    @image.setter
    def image(self, new_image):
        """
        Setter para o atributo image

        :param new_image: nova imagem
        :type new_image: pygame.surface.Surface
        """
        self.__image = new_image

    @direcao.setter
    def direcao(self, new_direction):
        """
        Setter do atributo direcao

        :param new_direction: nova direção da nave
        :type new_direction: int
        """
        self.__direcao = new_direction

    def move(self):
        """
        Método para definir o movimento do objeto pela tela e ciclo do ressurgimento
        """
        # Movimentação pelo eixo x
        self.rect.x += 1

        # Definindo a posição y
        if self.direcao == 0:
            self.rect.y = 50

        if self.direcao == 1:
            self.rect.y = ALTURA//2       

        # Definindo o ciclo de ressurgimento
        if self.rect.x > 2*LARGURA:
            self.rect.x = - LARGURA
            # Sorteando a posição do y
            self.direcao = randint(0,1)

    def update(self):
        """
        Método para atualizar a imagem, movimento e outras variáveis do objeto
        """
        # Alternando entre as imagens 
        if self.index_lista > 24:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.image_ufo[int(self.index_lista)]

        # Mover a nave pelo eixo x
        self.move()

        # Se a nave  estiver na tela a variável será verdadeira
        if self.rect.x > 10 and self.rect.x < LARGURA:
            self.atirar = 1
        else:
            self.atirar = 0

        # Antes de passar na tela, o efeito sonoro é ativado
        if self.rect.x == -100:
            ufo_sound.play()

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
    
    def move(self):
        """
        Método para movimentação do laser pela tela
        """
        # O laser será acionando se o alien estiver acima da tela
        if self.alien.direcao == 0:
            self.rect.y += 2

    def update(self):
        """
        Método para atualizar o movimento do objeto
        """
        # Atualizando as imagens e movimento
        self.move()