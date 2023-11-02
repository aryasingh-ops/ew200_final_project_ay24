import pygame
import sys

# initialize Pygame
pygame.init()

# set screen dimensions
SCREEN_WIDTH = 700
OUTBOUND_WIDTH = 150
SCREEN_HEIGHT = 400
WHITE_SNOW = (255, 255, 255)
TILE_SIZE = 16
SCALE_FACTOR = 1
# load an image for the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
blue_snow = pygame.image.load("ski_assets/ski_images/tile_0027.png").convert()

background = screen.copy()


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


draw_background()
# main game loop
while True:
    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw and display screen
    screen.blit(background, (0, 0))
    pygame.display.update()
    pygame.display.flip()
