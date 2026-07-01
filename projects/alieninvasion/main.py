import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    # Initializes the game, creates a display window
    pygame.init()
    # Creates an instance called ai_settings, which pulls from the Settings module
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)    
    bullets = Group()
    aliens = Group()
    pygame.display.set_caption("Alien Invaders")
    play_button = Button(ai_settings, screen, "Play")
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Starts the main game loop
    while True:

        # All of these functions are self contained in their own modules
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active: 
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

# Runs the game
run_game()