"""
Módulo contendo a geração e configuração das telas do jogo.
"""

import pygame

# Inicializando as fontes
pygame.font.init()

# Dimensões da tela do jogo
LARGURA = 600
ALTURA = 600

# Criando a tela
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space War")

# Fontes
font20 = pygame.font.SysFont("arialblack", 20, True, False)
font40 = pygame.font.SysFont("arialblack", 40, True, False)
font30 = pygame.font.SysFont("arialblack", 30, True, False)

# Textos da tela de game over
text_game_over_1 = "Fim de jogo"
formated_text_game_over_1 = font40.render(text_game_over_1, False, "white")
text_game_over_2 = "Aperte R para reiniciar"
formated_text_game_over_2 = font30.render(text_game_over_2, False, "white")