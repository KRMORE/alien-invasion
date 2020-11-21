import pygame.font

class Button():

        def __init__(self, ai_settings, screen, msg):
        
            self.screen = screen
            self.screen_rect = screen.get_rect()
            
            #set dimiensions of button
            self.width, self.height = 200, 50
            self.button_color = (151, 104, 255)
            self.button_color2 = (250, 179, 155)
            self.button_color3 = (0,0,0)
            
            self.text_color = (0, 0, 0)
            self.font = pygame.font.SysFont(None, 48)
            
            #bulid the button's rect
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect2 = pygame.Rect(0, 0, self.width+7, self.height+7)
            self.rect3 = pygame.Rect(0, 0, self.width+10, self.height+10)
            
            self.rect3.center = self.screen_rect.center
            self.rect2.top = self.rect3.top
            self.rect2.left = self.rect3.left
            self.rect.center = self.rect2.center
            
            self.prep_msg(msg)
            
        def prep_msg (self, msg):
            
            self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center
            
        def draw_button(self):
            
            self.screen.fill(self.button_color3, self.rect3)
            self.screen.fill(self.button_color2, self.rect2)
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)