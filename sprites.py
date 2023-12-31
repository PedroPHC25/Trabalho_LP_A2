"""
Módulo responsável por carregar e configurar as imagens utilizadas no jogo.
Elas são utilizadas na "main".
"""

import pygame
import os
from space_sprites import SpaceSprites

# Pasta atual
current_dir = os.path.dirname(os.path.abspath(__file__))

####################################################  PLAYER SHIP  ##########################################################

# Carregando a imagem da nave
img_ship = pygame.image.load(os.path.join(current_dir, "images/ship/Spaceship_tut.png"))
img_ship = pygame.transform.scale(img_ship, (img_ship.get_width()/3, img_ship.get_height()/3))

# Carregando a imagem dos tiros
img_shot = pygame.image.load(os.path.join(current_dir, "images/shot/20.png"))
img_shot = pygame.transform.scale(img_shot, (img_shot.get_width()/5, img_shot.get_height()/5))

# Lista com os caminhos de cada imagem de fundo
paths_images_space = []

# Adicionando cada caminho à lista
for image in os.listdir(os.path.join(current_dir, "images/space")):
    paths_images_space.append(os.path.join(os.path.join(current_dir, "images/space"), image))

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

################################################  BIG METEORO  ######################################################################

paths_images_big_meteor = []

for image in os.listdir(os.path.join(current_dir, "images/big_meteor")):
    paths_images_big_meteor.append(os.path.join(os.path.join(current_dir, "images/big_meteor"), image))


list_images_big_meteor = []

for each_image in paths_images_big_meteor:
    img_big_meteor = pygame.image.load(each_image)
    img_big_meteor= pygame.transform.scale(img_big_meteor, (img_big_meteor.get_width()/4, img_big_meteor.get_height()/4))
    list_images_big_meteor.append(img_big_meteor)


#####################################################  FIREBALL  ###################################################################

# Lista para armazenar os caminhos das imagens de fireball
paths_images_fireball = []

# Itera sobre os arquivos no diretório "images/fireball"
for image in os.listdir(os.path.join(current_dir, "images/fireball")):
    # Adiciona o caminho completo da imagem à lista
    paths_images_fireball.append(os.path.join(os.path.join(current_dir, "images/fireball"), image))

# Lista para armazenar as imagens de fireball
list_images_fireball = []

# Itera sobre cada caminho de imagem na lista
for each_image in paths_images_fireball:
    # Carrega a imagem usando Pygame
    img_fireball = pygame.image.load(each_image)
    
    # Redimensiona a imagem para um quarto do tamanho original
    img_fireball = pygame.transform.scale(img_fireball, (img_fireball.get_width() // 4, img_fireball.get_height() // 4))
    
    # Adiciona a imagem redimensionada à lista
    list_images_fireball.append(img_fireball)

 ################################################   ALIEN SHIP   ########################################################################

# Carregando as imagens da nave alien
paths_images_ufo = []

for image in os.listdir(os.path.join(current_dir, "images/ufo")):
    paths_images_ufo.append(os.path.join(os.path.join(current_dir, "images/ufo"), image))

list_images_ufo = []

for each_image in paths_images_ufo:
    img_ufo = pygame.image.load(each_image)
    img_ufo = pygame.transform.scale(img_ufo, (img_ufo.get_width()/6, img_ufo.get_height()/6))
    list_images_ufo.append(img_ufo)

# Carregando a imagem do laser
img_laser= pygame.image.load(os.path.join(current_dir, "images/laser/blue_laser.png"))
img_laser = pygame.transform.scale(img_laser, (img_laser.get_width()/5, img_shot.get_height()/5))
