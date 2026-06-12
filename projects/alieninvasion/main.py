import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Initializes the game, creates a display window
    pygame.init()
    # Creates an instance called ai_settings, which pulls from the Settings module.
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    ship = Ship(screen)
    
    pygame.display.set_caption("Alien Invaders")

    # Starts the main game loop
    while True:

        # Listens for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

# Runs the game
run_game()