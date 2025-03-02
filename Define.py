import pygame
import os

pygame.init()
#SCREEN
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
WIDTH_IMAGE = 500
HEIGHT_IMAGE = 200

#PATH
PATH_DICTIONARY = os.path.dirname((__file__))
PATH_IMAGE = os.path.join (PATH_DICTIONARY, "Images/")

#COLOR
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
PURPLE = (128, 0, 128)
ORGANGE = (255, 165, 0)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
CYAN = (0, 255, 255)

#PLAYER
PLAYER_RADIUS = 20
PLAYER_X = 20
PLAYER_Y = 800

