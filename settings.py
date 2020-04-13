
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
BACKGROUND = (95, 74, 32)

# Game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Journey of the Praire King"
ICON = "assets/img/icon.png"
BGCOLOR = BACKGROUND

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Wall settings
WALL_IMG = "wall.png"

# Player settings
PLAYER_SPEED = 120
PLAYER_IMG = "player.png"
PLAYER_HIT_RECT = pygame.Rect(10, 16, 25, 19)

# Gun settings
BULLET_IMG = "bullet.png"
BULLET_SPEED = 300
BULLET_LIFETIME = 2300
BULLET_RATE = 400

# Mob settings
MOB_IMG = "mob.png"
MOB_SPEED = 60
MOB_HIT_RECT = pygame.Rect(0, 0, 32, 32)