import pygame
from pygame.locals import *
from sys import exit
from screens import screen, LARGURA, ALTURA, font20, font30, formated_text_game_over_1, formated_text_game_over_2
from player import Ship, Shot
from sprites import imgs_space, list_images_big_meteor, list_images_fireball
from SpaceObjects import BigMeteor, Comet
from sounds import player_shot_sound, music
from alien import Ufo, Laser

# Inicializando o pygame
pygame.init()

# Tocando a música
pygame.mixer.music.play(-1)

# Relógio para controlar os ticks do jogo
clock = pygame.time.Clock()

def game_init():
    global all_sprites, all_enemies, all_stars, all_player_shots, player_shots_cooldown, shots, game_time, game_screen, ship, player_shots_cooldown, shots, alien_shot_cooldown, ufo,all_alien_shots, alien_group, alien_collision_cooldown
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
    # Variável para controlar o intervalo entre os tiros do player e ovni
    player_shots_cooldown = 50
    alien_shot_cooldown = 50
    alien_collision_cooldown = 0
    # Lista com todos os tiros
    shots = []
    #Criando os meteoros grandes 
    y = -50
    for i in range(3):
        big_meteor= BigMeteor(y, list_images_big_meteor)
        all_sprites.add(big_meteor)
        all_enemies.add(big_meteor)
        y = y - 700
    #Criando o cometa 
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
    # Tempo de jogo
    game_time = 0
    # Variável para checar se o player perdeu
    game_screen = "game"

game_init()

while True:
    clock.tick(60)
    screen.fill("black")

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
            if event.key == K_r and game_screen == "gameover":
                game_init()

    # Acionando o laser quando o ovni está na tela
    if ufo.atirar == True and alien_shot_cooldown > 150:
        laser_shot = Laser(ufo)
        all_sprites.add(laser_shot)
        all_enemies.add(laser_shot)
        alien_shot_cooldown = 0

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
    
    # Variável das colisões dos inimigos com a nave
    enemy_collisions = pygame.sprite.spritecollide(ship, all_enemies, True, pygame.sprite.collide_mask)

    if enemy_collisions:
        # Cria um novo meteoro no lugar do que foi destruído
        new_meteor = BigMeteor(-500, list_images_big_meteor)
        all_sprites.add(new_meteor)
        all_enemies.add(new_meteor)
        # Cria um novo cometa no lugar
        fireball = Comet(-500, list_images_fireball)
        all_sprites.add(fireball)
        all_enemies.add(fireball)
        # Dá dano na nave
        ship.take_damage()

    player_shot_collisions = pygame.sprite.groupcollide(all_player_shots, all_enemies, True, True, pygame.sprite.collide_mask)

    if player_shot_collisions:
        # Cria um novo meteoro no lugar do que foi destruído
        new_meteor = BigMeteor(-500, list_images_big_meteor)
        all_sprites.add(new_meteor)
        all_enemies.add(new_meteor)
        # Cria um novo cometa no lugar
        fireball = Comet(-500, list_images_fireball)
        all_sprites.add(fireball)
        all_enemies.add(fireball)
        game_time += 200

    # Adicionando uma colisão com o próprio ovni
    alien_collision = pygame.sprite.spritecollide(ship, alien_group, False)
    alien_collision_cooldown += 1

    # Definindo dano por segundo 
    if alien_collision_cooldown > 60 and alien_collision:
        ship.take_damage()
        alien_collision_cooldown = 0
        
    # Caso a vida chegue a 0, tela de game over
    if ship.health <= 0:
        game_screen = "gameover"

    # Texto da pontuação
    text_time = f"{game_time//10}"

    if game_screen == "game":
        # Atualiando as variáveis
        player_shots_cooldown += 1
        alien_shot_cooldown += 1
        game_time += 1
        # Desenhando e atualizando todas as sprites
        all_sprites.draw(screen)
        all_sprites.update()
        # Texto do tempo de jogo
        formated_text_time = font20.render(text_time, False, "white")
        screen.blit(formated_text_time, (500, 50))
        # Barra de vida
        pygame.draw.rect(screen, "white", (30, 30, 250, 10))
        pygame.draw.rect(screen, "red", (30, 30, ship.health*50, 10))
    elif game_screen == "gameover":
        all_stars.draw(screen)
        all_stars.update()
        formated_text_time = font30.render(text_time, False, "white")
        screen.blit(formated_text_game_over_1, (LARGURA/2 - formated_text_game_over_1.get_width()/2, 200))
        screen.blit(formated_text_time, (LARGURA/2 - formated_text_time.get_width()/2, 285))
        screen.blit(formated_text_game_over_2, (LARGURA/2 - formated_text_game_over_2.get_width()/2, 350))

    pygame.display.flip()