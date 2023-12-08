import pygame
from pygame.locals import *
from sys import exit
import screens as scr
from player import Ship, Shot
from sprites import imgs_space, list_images_big_meteor, list_images_fireball
from space_objects import BigMeteor, Comet
from sounds import player_shot_sound, destruction_sound, gameover_sound, damage_sound
from ufo import Ufo, Laser
from random import randrange

# Inicializando o pygame
pygame.init()

# Tocando a música
pygame.mixer.music.play(-1)

# Relógio para controlar os ticks do jogo
clock = pygame.time.Clock()

# Função para inicializar e resetar o jogo
def game_init():
    """
    Função que inicializa todos os objetos e variáveis do jogo.
    """
    global all_sprites, all_enemies, all_stars, all_player_shots, player_shots_cooldown, \
        shots, ship, player_shots_cooldown, shots, alien_shot_cooldown, \
        ufo, alien_group, alien_collision_cooldown, gameover_sound_played, \
        points, points_multiplier, spawn_cooldown, up_key, down_key, left_key, right_key
    # Grupo com todos os objetos que serão exibidos
    all_sprites = pygame.sprite.Group()
    # Grupo com todos os inimigos
    all_enemies = pygame.sprite.Group()
    # Grupo com todos os tiros do player e ovni
    all_player_shots = pygame.sprite.Group()
    alien_group = pygame.sprite.Group()
    # Grupo com os sprites das estrelas do fundo
    all_stars = pygame.sprite.Group()
    # Adicionando as imagens do fundo nos grupos
    for each_image in imgs_space:
        all_sprites.add(each_image)
        all_stars.add(each_image)
    # Criando a nave e adicionando-a ao grupo
    ship = Ship()
    all_sprites.add(ship)
    # Variáveis para controlar o intervalo entre os tiros do player e do ovni e do dano do alien
    player_shots_cooldown = 50
    alien_shot_cooldown = 50
    alien_collision_cooldown = 0
    # Lista com todos os tiros
    shots = []
    # Criando os meteoros grandes e adicionando-o ao grupo de todos os sprites e de inimigos
    y = -50
    for i in range(3):
        big_meteor= BigMeteor(y, list_images_big_meteor)
        all_sprites.add(big_meteor)
        all_enemies.add(big_meteor)
        y = y - 700
    # Criando o cometa e adicionando-o ao grupo de todos os sprites e de inimigos
    y = -50
    for i in range(2):
        fireball = Comet(y, list_images_fireball)
        all_sprites.add(fireball)
        all_enemies.add(fireball)
        y = y - 900
    # Criando o objeto ovni e adicionando na tela
    ufo = Ufo()
    all_sprites.add(ufo)
    alien_group.add(ufo)
    # Cooldown de spawn dos inimigos
    spawn_cooldown = 0
    # Pontuação
    points = 0
    points_multiplier = 0
    # Variável para checar se o player perdeu
    # Variável para controlar a reprodução do som de game over para tocar apenas 1 vez
    gameover_sound_played = False

# Teclas de controle
up_key = K_w
down_key = K_s
left_key = K_a
right_key = K_d

# Inicializando o jogo
game_init()
game_screen = "start"

while True:
    clock.tick(60)
    scr.screen.fill("black")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            # Criar um novo tiro e adicioná-lo ao grupo de sprites ao apertar a barra de espaço
            if event.key == K_SPACE and player_shots_cooldown > 50:
                new_shot = Shot(ship.x, ship.y - 40)
                all_sprites.add(new_shot)
                all_player_shots.add(new_shot)
                player_shots_cooldown = 0
                player_shot_sound.play()
            # Reiniciando o jogo ao apertar R
            if event.key == K_r and game_screen == "gameover":
                game_init()
                game_screen = "game"
            if game_screen == "start":
                # Começando o jogo com WASD ao apertar W
                if event.key == K_w:
                    game_screen = "game"
                # Começando o jogo com as setinhas ao apertar a setinha para cima
                if event.key == K_UP:
                    up_key = K_UP
                    down_key = K_DOWN
                    left_key = K_LEFT
                    right_key = K_RIGHT
                    game_screen = "game"

    # Acionando o laser quando o ovni está na tela e na parte de cima da tela
    if ufo.shoot == True and alien_shot_cooldown > 60 and ufo.direction == 0:
        laser_shot = Laser(ufo)
        all_sprites.add(laser_shot)
        all_enemies.add(laser_shot)
        alien_shot_cooldown = 0

    # Movimentação do player por WASD
    if pygame.key.get_pressed()[up_key] and not pygame.key.get_pressed()[left_key] and not pygame.key.get_pressed()[right_key]:
        ship.move("up")
    if pygame.key.get_pressed()[down_key] and not pygame.key.get_pressed()[left_key] and not pygame.key.get_pressed()[right_key]:
        ship.move("down")
    if pygame.key.get_pressed()[left_key] and not pygame.key.get_pressed()[up_key] and not pygame.key.get_pressed()[down_key]:
        ship.move("left")
    if pygame.key.get_pressed()[right_key] and not pygame.key.get_pressed()[up_key] and not pygame.key.get_pressed()[down_key]:
        ship.move("right")
    if pygame.key.get_pressed()[up_key] and pygame.key.get_pressed()[left_key]:
        ship.move("upleft")
    if pygame.key.get_pressed()[up_key] and pygame.key.get_pressed()[right_key]:
        ship.move("upright")
    if pygame.key.get_pressed()[down_key] and pygame.key.get_pressed()[left_key]:
        ship.move("downleft")
    if pygame.key.get_pressed()[down_key] and pygame.key.get_pressed()[right_key]:
        ship.move("downright")

    # Variável das colisões dos inimigos com a nave
    enemy_collisions = pygame.sprite.spritecollide(ship, all_enemies, True, pygame.sprite.collide_mask)

    if enemy_collisions:
        # Dá dano na nave
        ship.take_damage()
        damage_sound.play()

    # Variável das colisões dos tiros da nave com os inimigos
    player_shot_collisions = pygame.sprite.groupcollide(all_player_shots, all_enemies, True, True, pygame.sprite.collide_mask)

    if player_shot_collisions:
        # Ganha pontos ao destruir o inimigo
        points += 200
        destruction_sound.play()

    # Adicionando uma colisão com o próprio ovni
    alien_collision = pygame.sprite.spritecollide(ship, alien_group, False)
    alien_collision_cooldown += 1

    # Definindo dano por segundo 
    if alien_collision_cooldown > 60 and alien_collision:
        ship.take_damage()
        alien_collision_cooldown = 0

    # Dá um de vida à nave a cada 100 pontos
    if points//1000 > points_multiplier:
        ship.increase_health()
        points_multiplier += 1
        
    # Spawna novos inimigos de tempos em tempos
    if spawn_cooldown > 180:
        # Novo meteoro
        new_meteor = BigMeteor(randrange(-800, -200), list_images_big_meteor)
        all_sprites.add(new_meteor)
        all_enemies.add(new_meteor)
        # Novo cometa
        fireball = Comet(randrange(-800, -200), list_images_fireball)
        all_sprites.add(fireball)
        all_enemies.add(fireball)
        spawn_cooldown = 0

    # Caso a vida chegue a 0, tela de game over
    if ship.health <= 0:
        game_screen = "gameover"
        # Tocando o som de morte apenas uma vez
        if gameover_sound_played == False:
            gameover_sound.play()
            gameover_sound_played = True

    # Texto da pontuação
    text_time = f"{points//10}"

    # Configuração das telas
    if game_screen == "game":
        # Atualiando as variáveis
        player_shots_cooldown += 1
        alien_shot_cooldown += 1
        points += 1
        spawn_cooldown += 1
        # Desenhando e atualizando todas as sprites
        all_sprites.draw(scr.screen)
        all_sprites.update()
        # Texto do tempo de jogo
        formated_text_time = scr.font20.render(text_time, False, "white")
        scr.screen.blit(formated_text_time, (500, 20))
        # Barra de vida
        pygame.draw.rect(scr.screen, "white", (30, 30, 250, 10))
        pygame.draw.rect(scr.screen, "red", (30, 30, ship.health*50, 10))
    elif game_screen == "gameover":
        # Continua desenhando as estrelas
        all_stars.draw(scr.screen)
        all_stars.update()
        # Textos da tela de game over
        formated_text_time = scr.font30.render(text_time, False, "white")
        scr.screen.blit(scr.formated_text_game_over_1, (scr.LARGURA/2 - scr.formated_text_game_over_1.get_width()/2, 200))
        scr.screen.blit(formated_text_time, (scr.LARGURA/2 - formated_text_time.get_width()/2, 285))
        scr.screen.blit(scr.formated_text_game_over_2, (scr.LARGURA/2 - scr.formated_text_game_over_2.get_width()/2, 350))
    elif game_screen == "start":
        # Continua desenhando as estrelas
        all_stars.draw(scr.screen)
        all_stars.update()
        # Textos da tela de start
        scr.screen.blit(scr.formated_text_start_1, (scr.LARGURA/2 - scr.formated_text_start_1.get_width()/2, 200))
        scr.screen.blit(scr.formated_text_start_2, (scr.LARGURA/2 - scr.formated_text_start_2.get_width()/2, 350))
        scr.screen.blit(scr.formated_text_start_3, (scr.LARGURA/2 - scr.formated_text_start_3.get_width()/2, 375))
        scr.screen.blit(scr.formated_text_start_4, (scr.LARGURA/2 - scr.formated_text_start_4.get_width()/2, 400))

    pygame.display.flip()