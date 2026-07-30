# We import pygame in this
# module because of the functionality
# we need to add in this class, which is
# located in pygame.
import pygame

class Ship:
    """A class to model a game element, such as a ship."""


    def __init__(self, ai_game):
        """Initialie attributes for the ships behavior."""
        self.screen = ai_game.screen  # Obtain screen object first.
        # Set obtain settings module
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  # Then establish the screen's rect.
        
        # Give path to image file and load to the screen.
        self.image = pygame.image.load('images/ship.bmp')
        # Establish the images rect first.
        self.image_rect = self.image.get_rect()

        # Start the ship element at the bottom center
        # of the screen.
        # This line is access an attribute held within image_rect.
        self.image_rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.image_rect.x)
        

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on a movement flag."""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.image_rect.left > 0:
            self.x -= self.settings.ship_speed

        # Assigning the converted float value to image_rect.x
        self.image_rect.x = self.x

    def blitme(self):
        """Use the blit function to load the image to screen surface."""
        self.screen.blit(self.image, self.image_rect)