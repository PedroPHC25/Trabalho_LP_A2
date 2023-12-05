import pygame
from pygame.locals import *
from sys import exit
from screens import screen, LARGURA, ALTURA
from player import Ship, Shot
from sprites import imgs_space

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

for each_image in imgs_space:
    all_sprites.add(each_image)

ship = Ship()
all_sprites.add(ship)

shots_cooldown = 50
shots = []

while True:
    clock.tick(60)
    screen.fill("black")
    shots_cooldown += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and shots_cooldown > 50:
                new_shot = Shot(ship.x, ship.y)
                all_sprites.add(new_shot)
                shots_cooldown = 0

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

    for each_sprite in all_sprites:
        if isinstance(each_sprite, Shot) and each_sprite.y < -50:
            all_sprites.remove(each_sprite)

    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()