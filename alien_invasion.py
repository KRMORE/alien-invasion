import sys
import pygame
from pygame.sprite import Group
from bullet import Bullet
from setting import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import pygame.mixer as mixer
import pygame.mixer_music as mixer_music

def run_game():

        #Initialize game and creat a screen object
        pygame.init()
        mixer.init()

        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        ship = Ship(screen, ai_settings)
       
        play_button = Button(ai_settings, screen, "Play")
       
        bullets = Group()
        aliens = Group()
        
        #Load Music files 
        background = mixer.Sound("img/back.wav")
        background.set_volume(5)
        hit = mixer.Sound("img\shoot.wav")
        
        #creat a fleet
        gf.create_fleet(ai_settings, screen, ship, aliens)
        
        #Create an instsnce to store game statistic and scoreboard
        stats = GameStats(ai_settings)
        sb = Scoreboard(ai_settings, screen, stats)
        
        # start main loop
        while True:
            
            gf.check_events(ai_settings, screen, stats, sb,  play_button,  ship, aliens,  bullets, background)
            background.play()
            gf.update_screen(ai_settings, screen, stats, sb,  ship, aliens,bullets, play_button)
            if stats.game_active:
                gf.update_bullets(ai_settings, screen, stats, sb,  ship, aliens, bullets, hit, background)
                gf.update_aliens(ai_settings ,screen, stats, sb, ship,  aliens, bullets)
                gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,bullets, play_button)
                
               

run_game()               