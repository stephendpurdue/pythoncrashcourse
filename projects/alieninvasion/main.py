import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Initializes the game, creates a display window
    pygame.init()
    # Creates an instance called ai_settings, which pulls from the Settings module
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    ship = Ship(ai_settings, screen)    
    bullets = Group()
    pygame.display.set_caption("Alien Invaders")

    # Starts the main game loop
    while True:

        # All of these functions are self contained in their own modules
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

# Runs the game
run_game()