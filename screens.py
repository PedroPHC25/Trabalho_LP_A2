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
font20 = pygame.font.SysFont("gillsans", 20, False, False)
font40 = pygame.font.SysFont("gillsans", 40, False, False)
font30 = pygame.font.SysFont("gillsans", 30, False, False)
font60 = pygame.font.SysFont("gillsans", 60, False, False)

# Textos da tela de game over
text_game_over_1 = "Fim de jogo"
formated_text_game_over_1 = font40.render(text_game_over_1, False, "white")
text_game_over_2 = "Aperte R para reiniciar"
formated_text_game_over_2 = font30.render(text_game_over_2, False, "white")

# Textos da tela de start
text_start_1 = "Space War"
formated_text_start_1 = font60.render(text_start_1, False, "white")
text_start_2 = "Aperte W para começar com WASD"
formated_text_start_2 = font20.render(text_start_2, False, "white")
text_start_3 = "Aperte seta para cima para começar com as setas"
formated_text_start_3 = font20.render(text_start_3, False, "white")
text_start_4 = "Aperte espaço para atirar"
formated_text_start_4 = font20.render(text_start_4, False, "white")