import pygame
from screens import LARGURA, ALTURA
import sprites as spr
from pygame.locals import QUIT, KEYDOWN
from random import randint
from sounds import ufo_sound

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ufo = spr.list_images_ufo

        self.index_lista = 0
        self.image = self.image_ufo[self.index_lista]

        self.rect = self.image.get_rect()

        self.rect.x = - LARGURA
        self.rect.y = 10
        
        self.direcao = 0
        self.atirar = False

    def update(self):
        if self.index_lista > 24:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.image_ufo[int(self.index_lista)]
        self.move()

        if self.rect.x > 10 and self.rect.x < LARGURA:
            self.atirar = True
        else:
            self.atirar = False

        if self.rect.x == -100:
            ufo_sound.play()

    def move(self):
        if self.direcao == 0:
            ufo.rect.y = 10
            ufo.rect.x += 1

        if self.direcao == 1:
            ufo.rect.y = 540
            ufo.rect.x += 1        

        if ufo.rect.x > 2*LARGURA:
            ufo.rect.x = - 3*LARGURA
            self.direcao = randint(0,1)

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

ufo = Alien()
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
        # if event.type == KEYDOWN:
            # Criar um novo tiro e adicioná-lo ao grupo de sprites ao apertar a barra de espaço
    if ufo.atirar == True and shots_cooldown > 100:
        # Criar um novo tiro e adicioná-lo ao grupo de sprites ao apertar a barra de espaço:
        new_shot = Laser(ufo)
        todas_sprites.add(new_shot)
        all_player_shots.add(new_shot) 
        shots_cooldown = 0    

    todas_sprites.draw(tela)
    todas_sprites.update()


    pygame.display.flip()

    