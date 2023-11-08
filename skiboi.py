import pygame
from settings import *


class SkiBoi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ski_assets/ski_images/tile_0071.png").convert()
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left:
            self.rect.x -= 10

        elif self.moving_right:
            self.rect.x += 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)


skiboi = pygame.sprite.Group()
