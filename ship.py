import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

        def __init__(self, screen, ai_setting):
        
                super(Ship, self).__init__()
                self.screen = screen
                self.ai_setting = ai_setting
                #Load image
               
                
                
                self.image = pygame.image.load('img/s.png')
                self.rect = self.image.get_rect()
                self.screen_rect = screen.get_rect()
                
                #Start new ship at a definite position of the screen
                self.rect.centerx = self.screen_rect.centerx
                self.rect.bottom = self.screen_rect.bottom
        
                #save a int value as float
                self.centerx = float(self.rect.centerx)
                
                # Movement flag
                self.moving_right = False
                self.moving_left = False
                
        
        def update(self ):
                if self.moving_right and self.rect.right  <= self.screen_rect.right:
                        self.centerx += self.ai_setting.ship_speed_factor
                        
               
                        
                if self.moving_left and self.rect.left  >= self.screen_rect.left + 15:
                        self.centerx -=self.ai_setting.ship_speed_factor
                        
                
                        
                #update the value of rect,center
                self.rect.centerx = self.centerx
                

        def center_ship(self):
                
                self.center = self.screen_rect.centerx
        def blitme(self):
                self.screen.blit(self.image, self.rect)