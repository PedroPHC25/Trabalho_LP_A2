import pygame

# Classe das imagens de fundo
class SpaceSprites(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        # Imagens do objeto
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (600, 600))
        # Coordenadas das imagens
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    # Método para movimentar as imagens de fundo
    def update(self):
        self.y = self.y + 1
        self.rect.topleft = (self.x, self.y)
        # A imagem volta para cima quando sai da tela por baixo
        if self.y > 600:
            self.y = -600