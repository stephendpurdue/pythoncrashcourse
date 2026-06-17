import pygame

class Character():

    def __init__(self, screen):
        self.screen = screen

        # Loads image and creates rec objects
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Positional arguments
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centerx = self.screen_rect.centerx

    # Draws image to screen
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    