import pygame

class Background:
    """A class to represent a game background for the pygame window."""

    def __init__(self, ai_game):
        """Initialize attributes for class."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/space.bmp')
        self.image_rect = self.image.get_rect()

        self.image_rect.center = self.screen_rect.center

    def blitme(self):
        """Draw background image to window."""
        self.screen.blit(self.image, self.image_rect)
