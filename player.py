import pygame
from Define import *


class Player:
    x = 0
    y = 0
    color = ""

    def __init__(self, money=1500):
        self.money = money
        self.index = 0

    def move(self, steps):
        self.index = (self.index + steps) % TOTAL_TILES

    def draw(self):
        if self.index == 0:
            x = BIG_TILE_SIZE // 2
            y = BIG_TILE_SIZE // 2 + TILE_SIZE_ROW * NUM_VERTICAL_TILES_UP + 50
        elif self.index < NUM_VERTICAL_TILES_UP:
            x = TILE_SIZE_ROW // 2
            y = HEIGHT - (self.index + 1) * TILE_SIZE_ROW + TILE_SIZE_ROW // 2 - 15
        elif self.index <= NUM_VERTICAL_TILES_UP:
            x = BIG_TILE_SIZE // 2
            y = BIG_TILE_SIZE // 2
        elif self.index < NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT:
            x = (self.index - NUM_VERTICAL_TILES_UP + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 - 37
            y = TILE_SIZE_COLUMN // 2
        elif self.index <= NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT:
            x = BIG_TILE_SIZE // 2 + NUM_HORIZONTAL_TILES_RIGHT * TILE_SIZE_ROW + 60
            y = BIG_TILE_SIZE // 2
        elif self.index < NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN:
            x = WIDTH - TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 50
            y = (self.index - (
                        NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT) + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 - 45
        elif self.index <= NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN:
            x = BIG_TILE_SIZE // 2 + NUM_HORIZONTAL_TILES_RIGHT * TILE_SIZE_ROW + 60
            y = BIG_TILE_SIZE // 2 + NUM_VERTICAL_TILES_DOWN * TILE_SIZE_COLUMN + 60
        else:
            x = WIDTH - (self.index - (
                        NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN) + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 15
            y = HEIGHT - TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 20

        pygame.draw.circle(screen, RED, (x, y), PLAYER_RADIUS)


class property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None