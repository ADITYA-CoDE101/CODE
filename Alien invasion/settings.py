class Setting:
    def __init__(self) -> None:
        #screen setting.
        self.screen_width = 1000
        self.screen_hight = 800
        self.bg_color =  (230, 230, 230)
        
        # speed of the ship
        self.speed = 2.5
        self.ship_limit = 3
        

        # Bullet setting
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings 
        self.alien_speed = 2.0
        self.fleet_drop_speed = 20
        # feet_direction of 1 reoresents right; -1 represemt left
        

        # HOw quickly the game speeds up
        self.speedup_scale = 1.1

        self.fleet_direction = 1
