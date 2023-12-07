import pygame
from screens import LARGURA
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
        self.__image = self.__image_ufo[self.__index_lista]

        self.__rect = self.__image.get_rect()
        
        # Definindo onde vai ser a primeira geração do objeto
        self.__rect.x = - LARGURA
        self.__rect.y = 50
        
        self.__direcao = 0
        self.__atirar = 0
    
    @property
    def atirar(self):
        return self.__atirar
    
    @atirar.setter
    def atirar(self, new_atirar):
        self.__atirar = new_atirar

    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image
    
    @property
    def direcao(self):
        return self.__direcao


    def update(self):

        # Alternando entre as imagens 
        if self.__index_lista > 24:
            self.__index_lista = 0
        self.__index_lista += 0.25
        self.__image = self.__image_ufo[int(self.__index_lista)]

        # Mover a nave pelo eixo x
        self.move()

        # Se a nave  estiver na tela a variável será verdadeira
        if self.__rect.x > 10 and self.__rect.x < LARGURA:
            self.atirar = 1
        else:
            self.atirar = 0

        # Antes de passar na tela, o efeito sonoro é ativado
        if self.__rect.x == -100:
            ufo_sound.play()

    def move(self):
        # Movimentação pelo eixo x
        self.__rect.x += 1

        # Definindo o surgimento abaixo ou acima da tela
        if self.__direcao == 0:
            self.__rect.y = 50

        if self.__direcao == 1:
            self.__rect.y = 540       

        # Definindo o ciclo de ressurgimento
        if self.__rect.x > 2*LARGURA:
            self.__rect.x = - 2*LARGURA
            self.__direcao = randint(0,1)

# Definindo a classe que será o tiro do ovni
class Laser(pygame.sprite.Sprite):
    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self)
        # Adicionando imagem
        self.__image = spr.img_laser
        # Adicionando qual será o objeto que disparará o tiro
        self.__alien = alien

        # Adiconando as posições do tiro, a partir do alien
        self.__rect = self.__image.get_rect()
        self.__rect.center = (self.__alien.rect.center[0], self.__alien.rect.center[1] + 20)
    
    def move(self):
        # O laser será acionando se o alien estiver acima da tela
        if self.__alien.direcao == 0:
            self.__rect.y += 2
        else:
            pass

    def update(self):
        # Atualizando as imagens e movimento
        self.move()

    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image

    