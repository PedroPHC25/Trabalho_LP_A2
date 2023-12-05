import pygame

img_ship = pygame.image.load("images/spiked ship 3. small.blue_.PNG")
img_ship = pygame.transform.scale(img_ship, (img_ship.get_width()/2, img_ship.get_height()/2))

img_shot = pygame.image.load("images/beams.png")
img_shot = pygame.transform.scale(img_shot, (img_shot.get_width()/4, img_shot.get_height()/4))