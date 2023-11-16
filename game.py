import pygame
import sys
from obstacle import Tree, trees, RedFlag, flags, BlueBlocker, blue_block, Snowman, snowman
import skier
import random
from settings import *

# initialize Pygame
pygame.init()

# load an image for the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = screen.copy()
blue_snow = pygame.image.load("ski_assets/ski_images/tile_0027.png").convert()

my_skier = skier.SkiBoi(350, 20)
my_trees = Tree(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), SPEED)
trees.add(my_trees)
for _ in range(NUM_TREES):
    trees.add(Tree(random.randint(0, SCREEN_WIDTH),
                   random.randint(0, SCREEN_HEIGHT), SPEED))
my_flags = RedFlag(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH), random.randint(0, SCREEN_HEIGHT),
                   SPEED)
flags.add(my_flags)
for _ in range(NUM_FLAGS):
    flags.add(RedFlag(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH),
                      random.randint(0, SCREEN_HEIGHT), SPEED))
my_blocks = BlueBlocker(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), SPEED)
blue_block.add(my_blocks)
for _ in range(NUM_BLOCKS):
    blue_block.add(BlueBlocker(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH),
                               random.randint(0, SCREEN_HEIGHT), SPEED))
my_snowman = Snowman(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), SPEED)
snowman.add(my_snowman)
for _ in range(NUM_SNOWMAN):
    snowman.add(Snowman(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH),
                        random.randint(0, SCREEN_HEIGHT), SPEED))


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
clock = pygame.time.Clock()
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

    trees.draw(screen)
    trees.update()
    if random.randint(0, 100) < 5:  # Adjust the probability as needed
        new_trees = Tree(random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT, SPEED)
        my_trees.add(trees)

    flags.draw(screen)
    flags.update()
    if random.randint(0, 100) < 5:  # Adjust the probability as needed
        new_flags = RedFlag(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH), SCREEN_HEIGHT, SPEED)
        my_flags.add(flags)

    blue_block.draw(screen)
    blue_block.update()
    if random.randint(0, 100) < 5:  # Adjust the probability as needed
        new_blocks = BlueBlocker(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH), SCREEN_HEIGHT, SPEED)
        my_blocks.add(blue_block)

    snowman.draw(screen)
    snowman.update()
    if random.randint(0, 100) < 5:  # Adjust the probability as needed
        new_snowman = Snowman(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH), SCREEN_HEIGHT, SPEED)
        my_snowman.add(snowman)

    clock.tick(60)
    pygame.display.update()
    pygame.display.flip()
