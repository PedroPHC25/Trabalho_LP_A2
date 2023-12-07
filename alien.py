import pygame
from screens import LARGURA, ALTURA
import sprites as spr
from pygame.locals import QUIT
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
        self.rect.y = 10
        
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
        ufo.rect.x += 1

        # Definindo o surgimento abaixo ou acima da tela
        if self.direcao == 0:
            ufo.rect.y = 10

        if self.direcao == 1:
            ufo.rect.y = 540       

        # Definindo o ciclo de ressurgimento
        if ufo.rect.x > 2*LARGURA:
            ufo.rect.x = - 2*LARGURA
            self.direcao = randint(0,1)
            print(self.direcao)

class Laser(pygame.sprite.Sprite):
    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self)
        self.image = spr.img_laser
        self.alien = alien
        self.rect = self.image.get_rect()
        self.rect.center = (self.alien.rect.center[0], 2*self.alien.rect.center[1])
    
    def move(self):
        if self.alien.direcao == 0:
            self.rect.y += 2
        else:
            pass

    def update(self):
        self.move()

ufo = Ufo()
todas_sprites = pygame.sprite.Group()
todas_sprites.add(ufo)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()
all_player_shots = pygame.sprite.Group()
shots_cooldown = 50
while True:
    tela.fill((0,0,0))
    relogio.tick(90)
    
    shots_cooldown += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()   
    if ufo.atirar == True and shots_cooldown > 150:
        new_shot = Laser(ufo)
        todas_sprites.add(new_shot)
        all_player_shots.add(new_shot) 
        shots_cooldown = 0    

    todas_sprites.draw(tela)
    todas_sprites.update()


    pygame.display.flip()

    