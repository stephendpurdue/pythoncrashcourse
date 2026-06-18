import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for a single alien"""

    def __init__(self, ai_settings, screen): 
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loads image and creates rec objects
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Set initial position as top of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the position as a float
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien to the screen"""
        self.screen.blit(self.image, self.rect)
