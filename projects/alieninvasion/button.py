import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initial attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Dimensions
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the buttons rect and center it

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare button message

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Render msg as an image and center"""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color) # Boolean value dictates antialiasing
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center