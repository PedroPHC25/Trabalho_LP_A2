import pygame
from screens import LARGURA, ALTURA
import sprites as spr
from random import randint
from sounds import ufo_sound

# Definindo uma classes para o objeto ovni
class Ufo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Adicionando a imagem 
        self.__image_ufo = spr.list_images_ufo

        # Uma variável para alterna entre as imagens 
        self.__index_lista = 0
        self.__image = self.image_ufo[self.index_lista]

        self.__rect = self.image.get_rect()
        
        # Definindo onde vai ser a primeira geração do objeto
        self.rect.x = - LARGURA
        self.rect.y = 50
        
        self.__direcao = randint(0,1)
        self.__atirar = 0

    def update(self):

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

    # Prpriedades do objeto
    @property
    def atirar(self):
        return self.__atirar
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image
    
    @property
    def direcao(self):
        return self.__direcao
    
    @property
    def index_lista(self):
        return self.__index_lista
    
    @property
    def image_ufo(self):
        return self.__image_ufo
    
    # Setter dos atributos
    @atirar.setter
    def atirar(self, new_atirar):
        self.__atirar = new_atirar

    @index_lista.setter
    def index_lista(self, new_index):
        self.__index_lista = new_index

    @image.setter
    def image(self, new_image):
        self.__image = new_image

    @direcao.setter
    def direcao(self, new_direction):
        self.__direcao = new_direction

    def move(self):
        # Movimentação pelo eixo x
        self.rect.x += 1

        # Definindo o surgimento abaixo ou acima da tela
        if self.direcao == 0:
            self.rect.y = 50

        if self.direcao == 1:
            self.rect.y = ALTURA//2       

        # Definindo o ciclo de ressurgimento
        if self.rect.x > 2*LARGURA:
            self.rect.x = - 2*LARGURA
            self.direcao = randint(0,1)

# Definindo a classe que será o tiro do ovni
class Laser(pygame.sprite.Sprite):
    def __init__(self, alien):
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
        return self.__rect
    
    @property
    def image(self):
        return self.__image
    
    @property
    def alien(self):
        return self.__alien
    
    def move(self):
        # O laser será acionando se o alien estiver acima da tela
        if self.alien.direcao == 0:
            self.rect.y += 2

    def update(self):
        # Atualizando as imagens e movimento
        self.move()