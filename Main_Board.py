import pygame
from Define import *

def draw_board():
    screen.fill(WHITE)
    
    for i in range(NUM_VERTICAL_TILES_UP):
        if i == 0:
            x = 0
            y = HEIGHT - (i + 1) * BIG_TILE_SIZE + 35
            pygame.draw.rect(screen, BLACK, (x, y, BIG_TILE_SIZE + 5, BIG_TILE_SIZE), 2)
        else:
            x = 0
            y = HEIGHT - (i + 1) * TILE_SIZE_COLUMN - 13
            pygame.draw.rect(screen, BLACK, (x, y, 130, TILE_SIZE_COLUMN), 2)
    
    for i in range(NUM_HORIZONTAL_TILES_RIGHT):
        if i == 0:
            x = (i) * BIG_TILE_SIZE
            y = 0
            pygame.draw.rect(screen, BLACK, (x, y, BIG_TILE_SIZE, BIG_TILE_SIZE + 8), 2)
        else:
            x =(i + 1) * TILE_SIZE_ROW - 50
            y = 0
            pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE_ROW, 130), 2) 
    
    for i in range(NUM_VERTICAL_TILES_DOWN):
        if i == 0:
            x = WIDTH - BIG_TILE_SIZE + 64
            y = (i) * TILE_SIZE_COLUMN
            pygame.draw.rect(screen, BLACK, (x, y, BIG_TILE_SIZE + 7 , BIG_TILE_SIZE), 2)
        else:
            x = WIDTH - TILE_SIZE_COLUMN + 28
            y = (i + 1) * TILE_SIZE_COLUMN - 50
            pygame.draw.rect(screen, BLACK, (x, y, 145, TILE_SIZE_COLUMN), 2)
    
    for i in range(NUM_HORIZONTAL_TILES_LEFT):
        if i == 0:
            x = 1450
            y = 742
            pygame.draw.rect(screen, BLACK, (x, y, BIG_TILE_SIZE + 2, BIG_TILE_SIZE + 7), 2)
        else:
            x = WIDTH - (i + 1) * TILE_SIZE_ROW + 15
            y = HEIGHT -  TILE_SIZE_ROW
            pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE_ROW, 140), 2)