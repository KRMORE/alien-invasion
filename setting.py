import pygame

class Settings():

    #to store all settings
        def __init__(self):
                """Initialize the game's settings"""
                #Screem Setting
                self.screen_width = 1200
                self.screen_height = 600
                back = pygame.image.load('img/back.bmp')
                self.bg_color = back
                
                #Ship speed
                self.ship_speed_factor = 1
                self.ship_limit = 3
                
                #bullet
                self.bullet_height = 20
                self.bullet_width = 5
                self.bullet_speed_factor = 2
                self.bullet_color = 255, 255, 30
                self.bullets_allowed = 199
                
                #alien speed
                self.alien_speed_factor = 1
                self.fleet_drop_speed = 5
                #fleet direction 
                self.fleet_direction = -1
                
                
                #game speed up speed
                self.speedup_scale = 1.75
                
                #points value speed up speed
                self.score_scale = 1.5
                
                self.initialize_dynamic_settings()
        
        def initialize_dynamic_settings(self):
                """change while game is on"""
                self.ship_speed_factor = 1.5
                self.bullet_speed_factor = 3
                
                self.alien_speed_factor = 2
                
                self.fleet_direction = 1
                
                #scoring
                self.alien_points = 50
                
        def increase_speed(self):
            """Increse setting"""
            self.ship_speed_factor *= self.speedup_scale
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale
            
            
            self.alien_points = int(self.alien_points * self.score_scale)
            