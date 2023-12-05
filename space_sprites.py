import pygame

class SpaceSprites(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (600, 600))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        self.y = self.y + 1
        self.rect.topleft = (self.x, self.y)
        if self.y > 600:
            self.y = -600