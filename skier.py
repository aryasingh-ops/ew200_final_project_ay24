import pygame
from settings import *


class SkiBoi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ski_assets/ski_images/tile_0071.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.x = x
        self.y = y
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left:
            self.x -= 0.5
        elif self.moving_right:
            self.x += 0.5
        self.rect.center = (self.x, self.y)
        if self.rect.left < OUTBOUND_WIDTH:
            self.rect.left = OUTBOUND_WIDTH
        if self.rect.right > SCREEN_WIDTH-OUTBOUND_WIDTH:
            self.rect.right = SCREEN_WIDTH-OUTBOUND_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)


skier = pygame.sprite.Group()
