import pygame
import os
from space_sprites import SpaceSprites

img_ship = pygame.image.load("images/spiked ship 3. small.blue_.PNG")
img_ship = pygame.transform.scale(img_ship, (img_ship.get_width()/2, img_ship.get_height()/2))

img_shot = pygame.image.load("images/beams.png")
img_shot = pygame.transform.scale(img_shot, (img_shot.get_width()/4, img_shot.get_height()/4))

paths_images_space = []

for image in os.listdir("images/space"):
    paths_images_space.append(os.path.join("images/space", image))

y_image_space = 0
imgs_space = []

for each_image in paths_images_space:
    image_space = SpaceSprites(0, y_image_space, each_image)
    imgs_space.append(image_space)
    y_image_space -= 600