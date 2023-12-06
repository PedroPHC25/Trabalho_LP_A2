"""
Módulo responsável por carregar e configurar as imagens utilizadas no jogo.
Elas são utilizadas na "main".
"""

import pygame
import os
from space_sprites import SpaceSprites

# Carregando a imagem da nave
img_ship = pygame.image.load("images\Spaceship_tut.png")
img_ship = pygame.transform.scale(img_ship, (img_ship.get_width()/3, img_ship.get_height()/3))

# Carregando a imagem dos tiros
img_shot = pygame.image.load("images/20.png")
img_shot = pygame.transform.scale(img_shot, (img_shot.get_width()/5, img_shot.get_height()/5))

# Carregando a imagem do cometa verde
img_green_comet = pygame.image.load("images/green_comet.png")
img_green_comet = pygame.transform.scale(img_green_comet, (img_green_comet.get_width()/5, img_green_comet.get_height()/5))

# Lista com os caminhos de cada imagem de fundo
paths_images_space = []

# Adicionando cada caminho à lista
for image in os.listdir("images/space"):
    paths_images_space.append(os.path.join("images/space", image))

# Coordenada y da primeira imagem de fundo
y_image_space = 0

# Lista com as imagens de fundo
imgs_space = []

for each_image in paths_images_space:
    # Criando cada imagem como um objeto da classe SpaceSprites
    image_space = SpaceSprites(0, y_image_space, each_image)
    # Adicionando cada imagem à lista
    imgs_space.append(image_space)
    # Alterando o y para a próxima imagem
    y_image_space -= 600

#############################################################################################
paths_images_big_meteor = []

for image in os.listdir("images/big_meteor"):
    paths_images_big_meteor.append(os.path.join("images/big_meteor", image))


list_images_big_meteor = []

for each_image in paths_images_big_meteor:
    img_big_meteor = pygame.image.load(each_image)
    img_big_meteor= pygame.transform.scale(img_big_meteor, (img_big_meteor.get_width()/4, img_big_meteor.get_height()/4))
    list_images_big_meteor.append(img_big_meteor)

#############################################################################################

# Carregando as imagens da nave alien
paths_images_ufo = []

for image in os.listdir("images/ufo"):
    paths_images_ufo.append(os.path.join("images/ufo", image))

list_images_ufo = []

for each_image in paths_images_ufo:
    img_ufo = pygame.image.load(each_image)
    img_ufo = pygame.transform.scale(img_ufo, (img_ufo.get_width()/6, img_ufo.get_height()/6))
    list_images_ufo.append(img_ufo)