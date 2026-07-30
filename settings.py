class Settings:
    """A class to store all settings for the class AlienInvasion."""

    def __init__(self):
        """Initialize game setings."""

        # Screen settings.
        # Also, always be sure to add a comment
        # before your new set of functionality for
        # the game to ensure clarity when someone
        # looks at your code.
        self.screen_width = 980
        self.screen_height = 660
        self.screen_color = (255, 255, 255)
        # Music.
        # Sound effect.
        # Display a start game screen before playing it.

        # Ship settings.
        self.ship_speed = 1.5

        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_width = 3 
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        