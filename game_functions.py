import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
import json
from pygame import mixer_music


def music_play():
    pass

def store_highscore(high_score):
    
    no = int(high_score)
    file = 'no.json'
    with open(file, 'w') as file:
        json.dump(no, file) 
        
def  check_aliens_bottom(ai_settings, screen, stats, sb,  ship, aliens, bullets):
        
        screen_rect = screen.get_rect()
        for alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
                break

def ship_hit(ai_settings,  screen, stats, sb,  ship, aliens, bullets):
        
        if stats.ship_left > 0:
                stats.ship_left -= 1
                
                #update score board
                sb.prep_ships()
                
                aliens.empty()
                bullets.empty()
                
                create_fleet(ai_settings, screen, ship, aliens)
                ship.center_ship()
                
                #pause.
                sleep(0.5)
        else:
                stats.game_active = False
                pygame.mouse.set_visible(True)

def get_number_aliens_x(ai_settings, alien_width):
         available_space_x = ai_settings.screen_width - 3 * alien_width
         number_aliens_x = int(available_space_x / (3 * alien_width))
         return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2*alien_width*alien_number 
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
        
        available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = int(available_space_y/ (3 * alien_height))
        return number_rows

def check_fleet_edges(ai_settings, aliens):
        """Respond edgw"""
        for alien in aliens.sprites():
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break

def change_fleet_direction(ai_settings, aliens):
        """Dorp fleet"""
        for alien in aliens:
            alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1

def check_high_score(stats, sb):
        
        if stats.score > stats.high_score:
                stats.high_score = stats.score
                sb.prep_high_score()
                high_score = stats.high_score
                store_highscore(high_score)

def update_aliens(ai_settings, screen, stats, sb,  ship,  aliens, bullets):
        """Update alien"""
        check_fleet_edges(ai_settings, aliens)
        check_aliens_bottom(ai_settings,  screen, stats, sb,  ship, aliens, bullets)
        aliens.update()
        
        #check alien bullet collisions
        if pygame.sprite.spritecollideany(ship, aliens):
            ship_hit(ai_settings,  screen, stats, sb, ship, aliens, bullets)

def create_fleet(ai_settings, screen, ship,  aliens):
        """Creatye a fleet"""
        alien = Alien(ai_settings, screen)
        number_aliens_x  = get_number_aliens_x(ai_settings, alien.rect.width)
        number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
        
        #create the first row of the aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_keyup(event, ship):
        #check key up events 
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
           
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
           
        elif event.key == pygame.K_UP:
            ship.moving_up = False
            
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False 

def check_keydown(event, ai_settings, screen, ship, bullets, background):

        
        if event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_RIGHT:
            ship.moving_right = True
            
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
            
        elif event.key == pygame.K_UP:
            ship.moving_up = True
            
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
           
        elif event.key == pygame.K_SPACE:
                fire_bullet(ai_settings, screen, ship, bullets, background)

def fire_bullet(ai_settings, screen, ship, bullets, background):
        """Fire a bullet"""
        if len(bullets) <= ai_settings.bullets_allowed:
                    new_bullet = Bullet(ai_settings, screen, ship)
                    bullets.add(new_bullet)
                    
                    background.stop()

def update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets, hit, background):
        #kljdhdadhd
        bullets.update()
        # gwt rid of old bullets
        for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                            bullets.remove(bullet)
        
        check_bullet_alien_collision(ai_settings, screen, stats, sb,  ship, aliens, bullets, hit, background)
        
def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets, hit, background):
       collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
       if collisions:
            for aliens in collisions.values():
                stats.score += ai_settings.alien_points* len(aliens)
                
                background.stop()
                hit.play()
                sb.prep_score()
            check_high_score(stats, sb)
       if len(aliens) == 0:
            bullets.empty()
            ai_settings.increase_speed()
            
            # Increase level
            stats.level += 1
            sb.prep_level()
            
            create_fleet(ai_settings, screen, ship, aliens)

def check_events(ai_settings, screen,stats, sb,  play_button,  ship, aliens, bullets, background):
    #watch the user input via keyboard and mouse
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                  check_keydown(event, ai_settings, screen, ship, bullets, background)
            elif event.type == pygame.KEYUP:
                    check_keyup(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    check_play_button(ai_settings, screen, stats, sb,  play_button, ship, aliens, bullets,  mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb,  play_button, ship, aliens, bullets, mouse_x, mouse_y):
        
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        
        if button_clicked and not stats.game_active:
        
                #reset game setting
                ai_settings.initialize_dynamic_settings()
        
                #hide mouse cursor
                pygame.mouse.set_visible(False)
                stats.reset_stats()
                stats.game_active = True
                
                #reset scoreboard img
                sb.prep_score()
                sb.prep_high_score()
                sb.prep_level()
                sb.prep_ships()
                
                #empty
                aliens.empty()
                bullets.empty()
                
                #nwe agauin
                create_fleet(ai_settings, screen, ship, aliens)
                ship.center_ship()
                
def update_screen(ai_settings, screen, stats, sb,  ship, aliens, bullets, play_button):
         ship.update()
        
         screen.blit(ai_settings.bg_color, [0,0])
         #draw all bullets
         for bullet in bullets:
                bullet.draw_bullet()
         ship.blitme()
         aliens.draw(screen)
         
         sb.show_score()
         
         if not stats.game_active:
            play_button.draw_button()
         
         #Display the sceen after updateung it
         pygame.display.flip()