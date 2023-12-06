import pygame

pygame.mixer.init()

pygame.mixer.music.set_volume(0.5)
music = pygame.mixer.music.load("sounds/Interstellar Official Soundtrack _ First Step – Hans Zimmer _ WaterTower.mp3")

player_shot_sound = pygame.mixer.Sound("sounds/laser5.wav")
player_shot_sound.set_volume(0.2)