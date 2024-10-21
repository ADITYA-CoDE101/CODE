import pygame
from settings import Setting

class Ship:

    def __init__(self, ai_game):
        """Initioalize the ship and set its starting posiotion"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image
        self.image = pygame.image.load('E:/PYTHON/bookish/Part II/Chapter 12/add_image/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the botto center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Speed of the ship
        self.setting = Setting()
        # Store a flat for the ship's exact position or cordinate.
        self.x =float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Moven=ment flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """update the ships movements based on movement flag"""
        # Updating the ship's x valu not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: # Rght edge
            self.x += self.setting.speed
            print(f"\tx- {self.x} : y- {self.y}")

        elif self.moving_left and self.rect.left > 0:  # Left edge
            self.x -= self.setting.speed
            print(f"\tx- {self.x} : y- {self.y}")

        elif self.moving_up and self.rect.top > 0:  # top edge
            self.y -= self.setting.speed
            print(f"\tx- {self.x} : y- {self.y}")
            
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom: # bottom edge
            self.y += self.setting.speed2
            print(f"\tx- {self.x} : y- {self.y}")

        
        
        """Here we Update rect object from self.x"""
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """recentering the ship after collision."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x = 470.0
        self.y = 750.0

    def blitme(self):
        """Draw the ship at its current location/position."""
        self.screen.blit(self.image, self.rect)