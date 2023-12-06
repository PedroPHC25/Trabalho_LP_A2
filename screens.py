"""
Módulo contendo a geração e configuração das telas do jogo.
"""

import pygame

# Dimensões da tela do jogo
LARGURA = 600
ALTURA = 600

# Criando a tela
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space War") # Vamos decidir