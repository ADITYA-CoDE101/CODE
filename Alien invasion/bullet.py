import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """The bullet class inherits the Sprite class"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_hight)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """MOve the bullet up the screen"""
        # Update the exact position of thr bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect positon
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bulet to thr screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)