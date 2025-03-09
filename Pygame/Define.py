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
screen.fill((128,128,128))
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
ORANGE = (255, 165, 0)
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
VERTICAL_TILE_SIZE_X=100
VERTICAL_TILE_SIZE_Y=130
HORIZONTAL_TILE_SIZE_X=99
HORIZONTAL_TILE_SIZE_Y=130

#DICE SURFACE
dice_face1=pygame.transform.scale(pygame.image.load(os.path.join('Images','face1.png')),(50,50))
dice_face2=pygame.transform.scale(pygame.image.load(os.path.join('Images','face2.png')),(50,50))
dice_face3=pygame.transform.scale(pygame.image.load(os.path.join('Images','face3.png')),(50,50))
dice_face4=pygame.transform.scale(pygame.image.load(os.path.join('Images','face4.png')),(50,50))
dice_face5=pygame.transform.scale(pygame.image.load(os.path.join('Images','face5.png')),(50,50))
dice_face6=pygame.transform.scale(pygame.image.load(os.path.join('Images','face6.png')),(50,50))
dice={1:dice_face1,2:dice_face2,3:dice_face3,4:dice_face4,5:dice_face5,6:dice_face6}

#Total_TIle
TOTAL_TILES = NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN + NUM_HORIZONTAL_TILES_LEFT

#Dice
def roll_dice():
    dice1=random.randint(1,6)
    print_dice1=0
    dice2=random.randint(1,6)
    print_dice2=0
    while print_dice1 != dice1:
        print_dice1 = random.randint(1, 6)
        screen.blit(dice[print_dice1], (200, 300))
        pygame.display.update()
        pygame.time.delay(250)

    while print_dice2 != dice2:
        print_dice2 = random.randint(1, 6)
        screen.blit(dice[print_dice2], (300, 300))
        pygame.display.update()
        pygame.time.delay(250)

    return dice1,dice2