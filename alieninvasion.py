import sys

import pygame

from pygame import mixer

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

from background import Background

class AlienInvasion:
    """An attempt to model an arcade video game."""

    def __init__(self):
        """Initialize attributes for game resources and other assets."""
        # Initializeds background settings.
        pygame.init()
        # Initialize mixer for background music.
        mixer.init()
        # Remember how module imports work?
        # You can always access them directly
        # when you give the name of the module.
        # mixer.music.load('audio/astronauts-symphony.mp3')
        # mixer.music.play(-1)
        self.settings = Settings()

        # This is what creates the dimensions for the pygame game
        # window.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Displays caption for the name of the window.
        # Just like the title tag does for an HTML document.
        self.window_caption = pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        # self.background = Background(self)

        # Manage related elements into a group.
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Starts main game loop."""
        # Main game loop.
        while True:
            # Detects for keyboard and mouse events within loop.
            # Event loop that looks for any events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            # Verifies how sprites are currently
            # available in the game window before
            # and after being fired.
            # print(len(self.bullets))

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # Remember, anytime you are comparing
                    # an event.type against a specific event.
                    # You specify that in the following block
                    # or else Python won't know what to do because
                    # you didn't give specifity.
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """Determines keydown events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """Determines keyup events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullets(self):
        """Create bullet and add to bullet group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullets and get rid of old bullets."""
        # Updates bullet position.
        self.bullets.update()

        # Get rid of olf bullets.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # alien = Alien(self)
        # self.aliens.add(alien)
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.image_rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Update screen with new elements."""
        # Fill the surface screen with the color
        # specified, redrawing the screen on each
        # pass through the while loop.
        # The method acts on the screen surface
        # to fill it with a color. It takes only one argument.
        self.screen.fill(self.settings.screen_color)
        # Always set background object before the
        # game element because Python will draw the image
        # in front of the ship element.
        # self.background.blitme()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        # Without this function, the surface which is a part
        # of the screen would not be able to be updated with what
        # has been most recently drawn to it. 
        pygame.display.flip()


if __name__ == '__main__':
    # Create instance from class.
    ai = AlienInvasion()
    ai.run_game()