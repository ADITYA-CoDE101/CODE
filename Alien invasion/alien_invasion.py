from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import Gamestats
from button import Button
import sys
import pygame
from time import sleep

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Setting()

        self.clock = pygame.time.Clock()
        self.screen_color = self.settings.bg_color
        # Full screen mode
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hight))
        """self.screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN) --> For full screen"""
        pygame.display.set_caption("Faltu game")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  # Gorup to hold the bullets  in __init__().
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.stats = Gamestats(self)
        self.game_active = False

        self.paly_button = Button(self, "Play")
    

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_keydown_event(self, event):
        """Response to keypresses."""
        if event.key == pygame.K_RIGHT:
            #move the ship right
            '''self.ship.rect.x += 1'''
            self.ship.moving_right  = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit() 
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
            

    def _check_keyup_event(self, event):
        """Response to key release."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _check_play_button(self, mouse_pos):
        button_click = self.paly_button.rect.collidepoint(mouse_pos)
        if button_click and not self.game_active:
            self.stats.reset_stats()
            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

    def fire_bullets(self):
        """Create a nw bullet and addd it ti the bullets group.""" 
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)     
            self.bullets.add(new_bullet)
    

    def update_screen(self):
        """Update image of the screen, and flip to the new screen."""
        self.screen.fill(self.screen_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        # draw the play button
        if not self.game_active:
            self.paly_button.draw_button()

        pygame.display.flip()  # This flips tothe new screen.
    
    def _update_bullets(self):
        """ Update position of he bullets and get rid of old bullets"""
        self.bullets.update()

        # Get rid of the bullets tha have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)
        
        # check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bulets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width , alien_hieght = alien.rect.size

        current_x, current_y = alien_width, alien_hieght
        while current_y < (self.settings.screen_hight - 3 * alien_hieght):
            while current_x < (self.settings.screen_width - 2* alien_width):
                '''print(current_x)'''
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2*alien_hieght

    def _create_alien(self, x_position, y_position):
        """create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)    

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        '''self.ship_collision()'''
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("--Ship Hit!!--")
            self._ship_hit()

        if self.stats.ships_left == 0:
            print("--You lost--")
            sys.exit()

        # replaced by the _check_alien_botton
        '''for alien in self.aliens.copy():
            screen_rect = self.screen.get_rect()
            if alien.rect.bottom >= screen_rect.bottom:
                print("--You lost--")
                sys.exit()'''
        # Look for the aien hitting the bottom of the screen.
        self._check_aliens_bottom()
        

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    '''def ship_collision(self):
        for alien in self.aliens:
            if alien.rect.bottom == self.ship.rect.top:
                print("--Ship collided__You lost--")
                sys.exit()'''
    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0 :
        # decrement the ship_left
            self.stats.ships_left -= 1

            # Empty the screen 
            self.bullets.empty()
            self.aliens.empty()

            # creat a new fleet
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_hight:
                self._ship_hit()
                break
            

    def run_game(self):
        while True:
            self.check_event()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self.update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    AI = AlienInvasion()
    AI.run_game()