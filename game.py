import pygame
import sys
import skier
import random
from settings import *

# initialize Pygame
pygame.init()

# load an image for the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = screen.copy()
blue_snow = pygame.image.load("ski_assets/ski_images/tile_0027.png").convert()
tree = pygame.image.load("ski_assets/ski_images/tile_0006.png").convert()
red_flag = pygame.image.load("ski_assets/ski_images/tile_0035.png").convert()
blue_blocker = pygame.image.load("ski_assets/ski_images/tile_0033.png").convert()
snowman = pygame.image.load("ski_assets/ski_images/tile_0069.png").convert()
my_skier = skier.SkiBoi(350, 20)


def draw_background():
    # draw white background
    background.fill(WHITE_SNOW)
    # draw the two blue stripes that represent out of bounds
    x_right = (SCREEN_WIDTH - OUTBOUND_WIDTH)
    x_left = OUTBOUND_WIDTH
    for i in range(SCREEN_WIDTH // TILE_SIZE):
        for j in range(SCREEN_HEIGHT // (TILE_SIZE * SCALE_FACTOR)):
            background.blit(blue_snow, (x_right + TILE_SIZE * SCALE_FACTOR * i,
                                        TILE_SIZE * SCALE_FACTOR * j))
            background.blit(blue_snow, (x_left - TILE_SIZE * SCALE_FACTOR * (i + 1),
                                        TILE_SIZE * SCALE_FACTOR * j))
    for _ in range(15):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        background.blit(tree, (x, y))
    for _ in range(5):
        x = random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        background.blit(red_flag, (x, y))
    for _ in range(5):
        x = random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        background.blit(blue_blocker, (x, y))
    for _ in range(4):
        x = random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        background.blit(snowman, (x, y))


draw_background()
# main game loop
while True:
    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_skier.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_skier.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_skier.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_skier.moving_right = False

    # draw and display screen
    my_skier.update()
    screen.blit(background, (0, 0))
    my_skier.draw(screen)
    pygame.display.update()
    pygame.display.flip()
