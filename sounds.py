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

# Carregando o efeito sonoro do ovni
ufo_sound = pygame.mixer.Sound("sounds/alien_voice.mp3")
ufo_sound.set_volume(0.2)

# Carregando o som da destruição dos asteroides e cometas
destruction_sound = pygame.mixer.Sound("sounds/explosion_6.wav")
destruction_sound.set_volume(0.5)

# Carregando o som de dano na nave
damage_sound = pygame.mixer.Sound("sounds/explosion01.wav")
damage_sound.set_volume(0.3)

# Carregando o som da destruição da nave
gameover_sound = pygame.mixer.Sound("sounds/explosion1.mp3")
gameover_sound.set_volume(0.1)