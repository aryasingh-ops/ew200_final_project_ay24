import pygame
from settings import *


def intro_screen():
    pygame.init()

    font = pygame.font.Font("ski_assets/ski_fonts/Print.ttf", 36)
    introduction = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    text = font.render("SHRED!", True, (255, 69, 0))

    # Fill the background with a color
    introduction.fill((197, 224, 250))

    # Adjust the values as needed
    for i in range(0, SCREEN_WIDTH, TILE_SIZE):
        introduction.blit(WHITE_SNOW, (i, SCREEN_HEIGHT - TILE_SIZE))

    # Replace introduction with a suitable background surface
    # You can create a new surface and fill it with a color, or load an image as the background
    # For example, to create a background surface with a different color:
    # background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    # background_surface.fill((0, 0, 255))
    # introduction.blit(background_surface, (0, 0))

    introduction.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()