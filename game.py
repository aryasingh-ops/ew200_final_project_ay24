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

background_music = pygame.mixer.Sound("ski_assets/ski_music/mixkit-hollidays-690.mp3")
background_music.set_volume(0.1)
points_music = pygame.mixer.Sound("ski_assets/ski_music/video-game-bonus-wooden-chime-gamemaster-audio-1-00-00.mp3")
points_music.set_volume(1)

full_health = pygame.image.load("ski_assets/ski_images/corazon.png").convert()
full_health.set_colorkey((0, 0, 0))
new_size = (50, 55)
full_health_resized = pygame.transform.scale(full_health, new_size)
heart_positions = [(0, 35), (35, 35), (70, 35)]
player_heart_positions = [(580, 35), (615, 35), (650, 35)]
num_player_hearts = len(player_heart_positions)
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
my_player_active = False

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
game_over = False
# main game loop

while not game_over:
    background_music.play()
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            player_button_rect = player_resized.get_rect(topleft=(10, 195))
            if player_button_rect.collidepoint(mouse_pos):
                my_player_active = True
        if my_player_active:
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = home_resized.get_rect(topleft=(10, 115))
            if button_rect.collidepoint(mouse_pos):
                pygame.time.wait(10000)  # 1000 ms = 1s
                print("Game Paused")
            else:
                print("Game Resumed")
        clock.tick(60)
    # draw and display screen
    my_skier.update()
    screen.blit(background, (0, 0))
    my_skier.draw(screen)
    if my_player_active:
        my_player.update()
        my_player.draw(screen)

        score_points_player = pygame.sprite.spritecollide(my_player, snowman, True)

        for heart in range(num_player_hearts):
            if heart < num_player_hearts:
                screen.blit(full_health_resized, player_heart_positions[heart])

        player_hit_trees = pygame.sprite.spritecollide(my_player, trees, False)
        for tree in player_hit_trees:
            if my_player.rect.colliderect(tree.rect):
                if my_player.x < tree.rect.centerx:
                    my_player.x -= my_player.velocity
                else:
                    my_player.x += my_player.velocity
                if my_player.y < tree.rect.centery:
                    my_player.y -= my_player.velocity
                else:
                    my_player.y += my_player.velocity
        if len(player_hit_trees) > 0:
            print(f'You hit a tree! You are down a life')
        player_hit_flags = pygame.sprite.spritecollide(my_player, flags, False)
        for flag in player_hit_flags:
            if my_player.rect.colliderect(flag.rect):
                if my_player.x < flag.rect.centerx:
                    my_player.x -= my_player.velocity
                else:
                    my_player.x += my_player.velocity
                if my_player.y < flag.rect.centery:
                    my_player.y -= my_player.velocity
                else:
                    my_player.y += my_player.velocity
        if len(player_hit_flags) > 0:
            print(f'You hit a flag! You are down a life')
        player_hit_blocks = pygame.sprite.spritecollide(my_player, blue_block, False)
        for block in player_hit_blocks:
            if my_player.rect.colliderect(block.rect):
                if my_player.x < block.rect.centerx:
                    my_player.x -= my_player.velocity
                else:
                    my_player.x += my_player.velocity
                if my_player.y < block.rect.centery:
                    my_player.y -= my_player.velocity
                else:
                    my_player.y += my_player.velocity
        if len(player_hit_blocks) > 0:
            print(f'You hit a block! You are down a life')
        player_total_hits = len(player_hit_trees) + len(player_hit_blocks) + len(player_hit_flags)
        if player_total_hits >= 2:  # Adjust the threshold as needed
            num_player_hearts -= 1
            total_hits = 0  # Reset total_hits
            if num_player_hearts == 0:
                num_player_hearts = 0  # Ensure num_hearts doesn't go negative
                game_over = True

        score_text = game_font.render(f"SCORE: {PLAYER_SCORE}", True, (39, 48, 145))
        screen.blit(score_text, (570, 10))
        PLAYER_SCORE += len(score_points_player)
        if len(score_points_player) > 0:
            print(f" You hit a snowman! Your score is {PLAYER_SCORE}!")
            points_music.play()

    trees.draw(screen)
    trees.update()
    # If the random number is less than 5, create a new tree at a random x coordinate, at the top of the screen,
    # and with a specified speed (SPEED)
    if random.randint(0, 100) < 5:
        new_trees = Tree(random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT, SPEED)
        my_trees.add(trees)
    # Adjusting the 5 to a different value would change the probability
    # 5 is used based on the frequency of new trees appearing in the game.
    flags.draw(screen)
    flags.update()
    if random.randint(0, 100) < 5:
        new_flags = RedFlag(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH), SCREEN_HEIGHT, SPEED)
        my_flags.add(flags)

    blue_block.draw(screen)
    blue_block.update()
    if random.randint(0, 100) < 5:
        new_blocks = BlueBlocker(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH), SCREEN_HEIGHT, SPEED)
        my_blocks.add(blue_block)

    snowman.draw(screen)
    snowman.update()
    if random.randint(0, 100) < 5:
        new_snowman = Snowman(random.randint(OUTBOUND_WIDTH, SCREEN_WIDTH - OUTBOUND_WIDTH), SCREEN_HEIGHT, SPEED)
        my_snowman.add(snowman)

    score_points_skier = pygame.sprite.spritecollide(my_skier, snowman, True)
    SCORE += len(score_points_skier)
    if len(score_points_skier) > 0:
        print(f" You hit a snowman! Your score is {SCORE}!")
        points_music.play()

    hit_trees = pygame.sprite.spritecollide(my_skier, trees, False)
    for tree in hit_trees:
        # Check if the rectangular bounding box of the skier intersects with the tree's bounding box
        if my_skier.rect.colliderect(tree.rect):
            # Adjust the skiers position to resolve the collision
            # Check if the skier is to the left or right of the center of the tree horizontally
            if my_skier.x < tree.rect.centerx:
                # If to the left, move the skier to the left
                my_skier.x -= my_skier.velocity
            else:
                # If to the right, move the skier to the right
                my_skier.x += my_skier.velocity
            # Check if the skier is above or below the center of the tree vertically
            if my_skier.y < tree.rect.centery:
                # If above, move the skier upwards
                my_skier.y -= my_skier.velocity
            else:
                # If below, move the skier downwards
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

    home = game_font.render("10s PAUSE", True, (39, 48, 145))
    screen.blit(home, (10, 85))
    screen.blit(home_resized, (10, 115))

    player_text = game_font.render("ADD PLAYER", True, (39, 48, 145))
    screen.blit(player_text, (10, 155))
    screen.blit(player_resized, (10, 195))

    if total_hits >= 2:  # Adjust the threshold as needed
        num_hearts -= 1
        total_hits = 0  # Reset total_hits
        if num_hearts == 0:
            num_hearts = 0  # Ensure num_hearts doesn't go negative
            game_over = True

    score_text = game_font.render(f"SCORE: {SCORE}", True, (39, 48, 145))
    screen.blit(score_text, (10, 10))
    for heart in range(num_hearts):
        if heart < num_hearts:
            screen.blit(full_health_resized, heart_positions[heart])

    clock.tick(60)
    pygame.display.update()
    pygame.display.flip()

if not my_player_active:
    screen.fill((177, 222, 242))
    end_font = pygame.font.Font(None, 48)
    end_text = end_font.render(f"Game Over - Final Score: {SCORE}", True, (39, 48, 145))
    screen.blit(end_text, (150, 175))
else:
    screen.fill((177, 222, 242))
    end_font = pygame.font.Font(None, 48)
    game_over = end_font.render(f"Game Over", True, (39, 48, 145))
    ski_results = end_font.render(f"Player 1 Score: {SCORE}", True, (39, 48, 145))
    player_results = end_font.render(f"Player 2 Score: {PLAYER_SCORE}", True, (39, 48, 145))
    if SCORE > PLAYER_SCORE:
        game_result = end_font.render(f"Player 1 Wins!", True, (39, 48, 145))
    else:
        game_result = end_font.render(f"Player 2 Wins!", True, (39, 48, 145))
    screen.blit(ski_results, (150, 220))
    screen.blit(player_results, (150, 275))
    screen.blit(game_over, (150, 65))
    screen.blit(game_result, (150, 120))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
