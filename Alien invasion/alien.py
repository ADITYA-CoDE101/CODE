import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image 
        self.image = pygame.image.load("E:/PYTHON/bookish/Part II/Chapter 12/add_image/alien.bmp")
        self.rect  = self.image.get_rect()

        # Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
        
    def update(self):
            # move the aliens

        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x