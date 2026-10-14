class Settings:
    """A class to store all settings for the class AlienInvasion."""

    def __init__(self):
        """Initialize game setings."""
        self.screen_width = 980
        self.screen_height = 660
        self.screen_color = (255, 255, 255)

        # Ship settings.
        self.ship_speed = 1.5

        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_width = 3 
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        
