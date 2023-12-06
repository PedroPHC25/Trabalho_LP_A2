"""
Módulo responsável por carregar e configurar a música e os sons do jogo.
"""

import pygame

# Inicializando o mixer
pygame.mixer.init()

# Carregando a música de fundo
pygame.mixer.music.set_volume(0.5)
music = pygame.mixer.music.load("sounds/Interstellar Official Soundtrack _ First Step – Hans Zimmer _ WaterTower.mp3")

# Carregando o som do tiro do player
player_shot_sound = pygame.mixer.Sound("sounds/laser5.wav")
player_shot_sound.set_volume(0.2)