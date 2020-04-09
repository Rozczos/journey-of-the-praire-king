
import pygame

# Define colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Journey of the Praire King"
ICON = "assets/img/icon.png"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 120
PLAYER_IMG = "player.png"
PLAYER_HIT_RECT = pygame.Rect(10, 16, 25, 19)