import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
        """A class to represent a single alien in a fleet"""
        
        def __init__(self, ai_settings, screen):
        
                super(Alien, self).__init__()
                self.screen = screen
                self.ai_settings = ai_settings
                
                #load image of alien
                self.image = pygame.image.load('img/bee.png')
                self.rect = self.image.get_rect()
                
                #ailen's destination
                self.rect.x = self.rect.width - 50
                self.rect.y = self.rect.height - 50
                
                #store a dcimal values
                self.x = float(self.rect.x)
        
        def check_edges(self):
                
                screen_rect = self.screen.get_rect()
                if self.rect.right >= screen_rect.right:
                        return True
                elif self.rect.left <= 0:
                    return True
        
        def update(self):
                """move the alien"""
                self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
                self.rect.x = self.x
        
        def blitme(self):
                """draw ailen"""
                self.screen.blit(self.image, self.rect)