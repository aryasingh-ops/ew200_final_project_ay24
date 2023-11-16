import pygame
from settings import *


class SkiBoi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ski_assets/ski_images/tile_0071.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.velocity = 6
        self.x = x
        self.y = y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left:
            self.x -= self.velocity
        elif self.moving_right:
            self.x += self.velocity
        elif self.moving_up:
            self.y -= self.velocity/2
        elif self.moving_down:
            self.y += self.velocity

        self.rect.center = (self.x, self.y)

        if self.rect.left < OUTBOUND_WIDTH:
            self.rect.left = OUTBOUND_WIDTH
        if self.rect.right > SCREEN_WIDTH - OUTBOUND_WIDTH:
            self.rect.right = SCREEN_WIDTH - OUTBOUND_WIDTH
        if self.rect.top < SKIER_HEIGHT:
            self.rect.top = SKIER_HEIGHT
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT-SKIER_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)


skier = pygame.sprite.Group()
