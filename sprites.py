"""
Módulo responsável por carregar e configurar as imagens utilizadas no jogo.
Elas são utilizadas na "main".
"""

import pygame
import os
from space_sprites import SpaceSprites

# Carregando a imagem da nave
img_ship = pygame.image.load("images/spiked ship 3. small.blue_.PNG")
img_ship = pygame.transform.scale(img_ship, (img_ship.get_width()/2, img_ship.get_height()/2))

# Carregando a imagem dos tiros
img_shot = pygame.image.load("images/beams.png")
img_shot = pygame.transform.scale(img_shot, (img_shot.get_width()/4, img_shot.get_height()/4))

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