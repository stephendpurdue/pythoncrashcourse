class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 0.75

        # Bullet settings

        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.ultrawide_bullet_width = 288

        # Alien settings

        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 7.5
        self.fleet_direction = 1 # 1 is right, -1 is left.