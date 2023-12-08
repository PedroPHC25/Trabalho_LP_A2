"""
Módulo responsável por carregar e configurar a música e os sons do jogo.
"""

import pygame
import os

# Verifica se o código está sendo executado pelo Sphinx
if os.environ.get('READTHEDOCS') == 'True':
    # Simula a ausência de áudio durante a geração da documentação no ReadTheDocs
    class DummySound:
        @staticmethod
        def play():
            pass

    class DummyMixer:
        @staticmethod
        def init():
            pass

        @staticmethod
        def set_volume(volume):
            pass

    pygame = DummyMixer()
    pygame.mixer = DummyMixer()
    pygame.mixer.Sound = DummySound
else:
    # Importa o Pygame normalmente quando não está gerando documentação
    import pygame
    pygame.mixer.init()

# Pasta atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Inicializando o mixer
pygame.mixer.init()

# Carregando a música de fundo
pygame.mixer.music.set_volume(0.5)
music = pygame.mixer.music.load(os.path.join(current_dir, "sounds/Interstellar Official Soundtrack _ First Step – Hans Zimmer _ WaterTower.mp3"))

# Carregando o som do tiro do player
player_shot_sound = pygame.mixer.Sound(os.path.join(current_dir, "sounds/laser5.wav"))
player_shot_sound.set_volume(0.2)

# Carregando o efeito sonoro do ovni
ufo_sound = pygame.mixer.Sound(os.path.join(current_dir, "sounds/alien_voice.mp3"))
ufo_sound.set_volume(0.2)

# Carregando o som da destruição dos asteroides e cometas
destruction_sound = pygame.mixer.Sound(os.path.join(current_dir, "sounds/explosion_6.wav"))
destruction_sound.set_volume(0.5)

# Carregando o som de dano na nave
damage_sound = pygame.mixer.Sound(os.path.join(current_dir, "sounds/explosion01.wav"))
damage_sound.set_volume(0.3)

# Carregando o som da destruição da nave
gameover_sound = pygame.mixer.Sound(os.path.join(current_dir, "sounds/explosion1.mp3"))
gameover_sound.set_volume(0.1)