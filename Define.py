import pygame
import os
import random

pygame.init()
#SCREEN
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
WIDTH_IMAGE = 500
HEIGHT_IMAGE = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

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

#Tile_Size
TILE_SIZE_COLUMN = 99
TILE_SIZE_ROW = 100
BIG_TILE_SIZE = 150
NUM_VERTICAL_TILES_UP = 7
NUM_HORIZONTAL_TILES_RIGHT = 14
NUM_VERTICAL_TILES_DOWN = 7
NUM_HORIZONTAL_TILES_LEFT = 14

#Total_TIle
TOTAL_TILES = NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN + NUM_HORIZONTAL_TILES_LEFT

#Dice
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)