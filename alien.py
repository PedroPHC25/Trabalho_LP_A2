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
        self.image_ufo = spr.list_images_ufo

        # Uma variável para alterna entre as imagens 
        self.index_lista = 0
        self.image = self.image_ufo[self.index_lista]

        self.rect = self.image.get_rect()
        
        # Definindo onde vai ser a primeira geração do objeto
        self.rect.x = - LARGURA
        self.rect.y = 50
        
        self.direcao = 0
        self.atirar = False

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
            self.atirar = True
        else:
            self.atirar = False

        # Antes de passar na tela, o efeito sonoro é ativado
        if self.rect.x == -100:
            ufo_sound.play()

    def move(self):
        # Movimentação pelo eixo x
        self.rect.x += 1

        # Definindo o surgimento abaixo ou acima da tela
        if self.direcao == 0:
            self.rect.y = 50

        if self.direcao == 1:
            self.rect.y = 540       

        # Definindo o ciclo de ressurgimento
        if self.rect.x > 2*LARGURA:
            self.rect.x = - 2*LARGURA
            self.direcao = randint(0,1)

# Definindo a classe que será o tiro do ovni
class Laser(pygame.sprite.Sprite):
    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self)
        # Adicionando imagem
        self.image = spr.img_laser
        # Adicionando qual será o objeto que disparará o tiro
        self.alien = alien

        # Adiconando as posições do tiro, a partir do alien
        self.rect = self.image.get_rect()
        self.rect.center = (self.alien.rect.center[0], 2*self.alien.rect.center[1])
    
    
    def move(self):
        # O laser será acionando se o alien estiver acima da tela
        if self.alien.direcao == 0:
            self.rect.y += 2
        else:
            pass

    def update(self):
        # Atualizando as imagens e movimento
        self.move()

    