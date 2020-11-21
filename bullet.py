import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
       """A manager of bullets like a pa"""
       def __init__(self, ai_settings, screen, ship):
            """creat a bullet"""
            super(Bullet, self).__init__()
            self.screen = screen
            # data needed stored in various varibles
            self.bullet_shape_hor = pygame.Rect(0,0, ai_settings.bullet_height, ai_settings.bullet_width)
            self.bullet_shape_ver = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
            self.ship = ship
            
            # Create a bullet
            self.rect = self.bullet_shape_ver
            self.rect.centerx = self.ship.rect.centerx - 15
            self.rect.top = self.ship.rect.top

            
                
            #float value
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor


       def update(self):
             """Move trhe bullet"""
             #update position
             self.y -= self.speed_factor
             self.rect.y = self.y
           
                
       def draw_bullet(self):

            pygame.draw.rect(self.screen, self.color, self.rect)