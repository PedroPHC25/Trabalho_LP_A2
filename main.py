import pygame
from pygame.locals import *
from sys import exit
from screens import screen, LARGURA, ALTURA
from player import Ship, Shot
from sprites import imgs_space, list_images_big_meteor
from SpaceObjects import BigMeteor
from sounds import player_shot_sound, music

# Inicializando o pygame
pygame.init()

# Tocando a música
pygame.mixer.music.play(-1)

# Relógio para controlar os ticks do jogo
clock = pygame.time.Clock()

# Grupo com todos os objetos que serão exibidos
all_sprites = pygame.sprite.Group()

# Adicionando as imagens do fundo no grupo
for each_image in imgs_space:
    all_sprites.add(each_image)

# Criando a nave e adicionando-a ao grupo
ship = Ship()
all_sprites.add(ship)

# Variável para controlar o intervalo entre os tiros do player
shots_cooldown = 50

# Lista com todos os tiros
shots = []

#Criando os meteoros grandes 
y = -50
for i in range(5):
    big_meteor= BigMeteor(y, list_images_big_meteor)
    all_sprites.add(big_meteor)
    y = y - 250


# Adicionando o meteoro 1
# all_sprites.add(big_meteor)


while True:
    clock.tick(90)
    screen.fill("black")
    shots_cooldown += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            # Criar um novo tiro e adicioná-lo ao grupo de sprites ao apertar a barra de espaço
            if event.key == K_SPACE and shots_cooldown > 50:
                new_shot = Shot(ship.x, ship.y - 40)
                all_sprites.add(new_shot)
                shots_cooldown = 0
                player_shot_sound.play()

    # Movimentação do player por WASD
    if pygame.key.get_pressed()[K_w] and not pygame.key.get_pressed()[K_a] and not pygame.key.get_pressed()[K_d]:
        ship.move("up")
    if pygame.key.get_pressed()[K_s] and not pygame.key.get_pressed()[K_a] and not pygame.key.get_pressed()[K_d]:
        ship.move("down")
    if pygame.key.get_pressed()[K_a] and not pygame.key.get_pressed()[K_w] and not pygame.key.get_pressed()[K_s]:
        ship.move("left")
    if pygame.key.get_pressed()[K_d] and not pygame.key.get_pressed()[K_w] and not pygame.key.get_pressed()[K_s]:
        ship.move("right")
    if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_a]:
        ship.move("upleft")
    if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_d]:
        ship.move("upright")
    if pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_a]:
        ship.move("downleft")
    if pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_d]:
        ship.move("downright")

    # Checando se cada tiro já saiu da tela e, se sim, retirando-o do grupo de sprites
    # para parar de renderizá-lo
    for each_sprite in all_sprites:
        if isinstance(each_sprite, Shot) and each_sprite.y < -50:
            all_sprites.remove(each_sprite)   
    
    # Desenhando e atualizando todas as sprites
    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()