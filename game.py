import pygame
import sys

import player_two
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

full_health = pygame.image.load("ski_assets/ski_images/corazon.png").convert()
full_health.set_colorkey((0, 0, 0))
new_size = (50, 55)
full_health_resized = pygame.transform.scale(full_health, new_size)
heart_positions = [(0, 35), (35, 35), (70, 35)]
num_hearts = len(heart_positions)

home_button = pygame.image.load("ski_assets/ski_images/tile_0074.png").convert()
home_button.set_colorkey((0, 0, 0))
new_size_home = (30, 35)
home_resized = pygame.transform.scale(home_button, new_size_home)

player_two_button = pygame.image.load("ski_assets/ski_images/tile_0083.png").convert()
player_two_button.set_colorkey((0, 0, 0))
new_player_button = (30, 35)
player_resized = pygame.transform.scale(player_two_button, new_player_button)

game_font = pygame.font.Font("ski_assets/ski_fonts/Print.ttf", 36)

my_skier = skier.SkiBoi(SKIER_WIDTH, SKIER_HEIGHT)
my_player = player_two.SkiTwo(PLAYER_WIDTH, SCREEN_HEIGHT)

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


def draw_play_background():
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


draw_play_background()
clock = pygame.time.Clock()

# main game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_skier.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_skier.moving_right = True
            if event.key == pygame.K_UP:
                my_skier.moving_up = True
            if event.key == pygame.K_DOWN:
                my_skier.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_skier.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_skier.moving_right = False
            if event.key == pygame.K_UP:
                my_skier.moving_up = False
            if event.key == pygame.K_DOWN:
                my_skier.moving_down = False
        clock.tick(60)
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

    score_points = pygame.sprite.spritecollide(my_skier, snowman, True)
    SCORE += len(score_points)
    if len(score_points) > 0:
        print(f" You hit a snowman! Your score is {SCORE}!")

    hit_trees = pygame.sprite.spritecollide(my_skier, trees, False)
    for tree in hit_trees:
        if my_skier.rect.colliderect(tree.rect):
            if my_skier.x < tree.rect.centerx:
                my_skier.x -= my_skier.velocity
            else:
                my_skier.x += my_skier.velocity
            if my_skier.y < tree.rect.centery:
                my_skier.y -= my_skier.velocity
            else:
                my_skier.y += my_skier.velocity

    if len(hit_trees) > 0:
        print(f'You hit a tree! You are down a life')

    hit_flags = pygame.sprite.spritecollide(my_skier, flags, False)
    for flag in hit_flags:
        if my_skier.rect.colliderect(flag.rect):
            if my_skier.x < flag.rect.centerx:
                my_skier.x -= my_skier.velocity
            else:
                my_skier.x += my_skier.velocity
            if my_skier.y < flag.rect.centery:
                my_skier.y -= my_skier.velocity
            else:
                my_skier.y += my_skier.velocity
    if len(hit_flags) > 0:
        print(f'You hit a flag! You are down a life')

    hit_blocks = pygame.sprite.spritecollide(my_skier, blue_block, False)
    for block in hit_blocks:
        if my_skier.rect.colliderect(block.rect):
            if my_skier.x < block.rect.centerx:
                my_skier.x -= my_skier.velocity
            else:
                my_skier.x += my_skier.velocity
            if my_skier.y < block.rect.centery:
                my_skier.y -= my_skier.velocity
            else:
                my_skier.y += my_skier.velocity
    if len(hit_blocks) > 0:
        print(f'You hit a block! You are down a life')

    total_hits = len(hit_trees) + len(hit_blocks) + len(hit_flags)

    score_text = game_font.render(f"SCORE: {SCORE}", True, (39, 48, 145))
    screen.blit(score_text, (10, 10))
    for heart in range(num_hearts):
        if heart < num_hearts:
            screen.blit(full_health_resized, heart_positions[heart])

    paused = True
    home = game_font.render("10s PAUSE", True, (39, 48, 145))
    screen.blit(home, (10, 85))
    screen.blit(home_resized, (10, 115))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = home_resized.get_rect(topleft=(10, 115))

            if button_rect.collidepoint(mouse_pos):
                if paused:
                    pygame.time.wait(10000)  # 1000 ms = 1s
                    print("Game Paused")
                else:
                    print("Game Resumed")
                paused = paused

    player_text = game_font.render("ADD PLAYER", True, (39, 48, 145))
    screen.blit(player_text, (10, 155))
    screen.blit(player_resized, (10, 195))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            player_button_rect = player_resized.get_rect(topleft=(10, 195))
            if player_button_rect.collidepoint(mouse_pos):
                my_player.update()
                my_player.draw(screen)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        my_player.moving_left = True
                    if event.key == pygame.K_d:
                        my_player.moving_right = True
                    if event.key == pygame.K_w:
                        my_player.moving_up = True
                    if event.key == pygame.K_s:
                        my_player.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        my_player.moving_left = False
                    if event.key == pygame.K_d:
                        my_player.moving_right = False
                    if event.key == pygame.K_w:
                        my_player.moving_up = False
                    if event.key == pygame.K_s:
                        my_player.moving_down = False

    if total_hits >= 2:  # Adjust the threshold as needed
        num_hearts -= 1
        total_hits = 0  # Reset total_hits
        if num_hearts == 0:
            num_hearts = 0  # Ensure num_hearts doesn't go negative
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.update()
    pygame.display.flip()
