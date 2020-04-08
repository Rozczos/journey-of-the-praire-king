
import pygame, sys
from pygame.locals import *


class Game():
    def __init__(self):
        print("It's working")

        # General setup
        pygame.init()
        clock = pygame.time.Clock()

        # Setting up the main window
        screen_width = 1600
        screen_height = 900
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Journey of the Praire King')
        pygame.display.set_icon(pygame.image.load('assets/img/icon.png'))


        while True:
            #Handling input
            self.events()
            
            #Visuals
            screen.fill((0, 0, 0))

            # Updating the window 
            pygame.display.flip()
            clock.tick(60)
    

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        