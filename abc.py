import sys

import pygame

def run_game():
        """ Intializing game and creat a screen object"""
        pygame.init()
        screen = pygame.display.set_mode((1000,800))
        pygame.display.set_caption("Alien Invasion")
        
        # start the main loop for the game.
        while True:
        
                # Watch for keyboard and mouse events.
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit
                                
                # Make the most recently drawn screen visible.
                pygame.display.filp()

run_game()                