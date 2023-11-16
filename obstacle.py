import pygame
from settings import *
import random


class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("ski_assets/ski_images/tile_0006.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -self.rect.height:
            self.rect.y = SCREEN_HEIGHT
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class RedFlag(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("ski_assets/ski_images/tile_0035.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -self.rect.height:
            self.rect.y = SCREEN_HEIGHT
            self.rect.x = random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class BlueBlocker(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("ski_assets/ski_images/tile_0033.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -self.rect.height:
            self.rect.y = SCREEN_HEIGHT
            self.rect.x = random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Snowman(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("ski_assets/ski_images/tile_0069.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -self.rect.height:
            self.rect.y = SCREEN_HEIGHT
            self.rect.x = random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


trees = pygame.sprite.Group()
flags = pygame.sprite.Group()
blue_block = pygame.sprite.Group()
snowman = pygame.sprite.Group()
