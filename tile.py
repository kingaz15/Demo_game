import pygame.transform

from player import Player
from Define import *


class StartTile:
    def __init__(self, x=50, y=650):
        self.x = x
        self.y = y
        self.reward = 200

    def pass_though(self, player):
        if (player.pre_x > self.x and player.x <= self.x and player.pre_y == self.y) or (
                player.pre_y < self.y and player.y >= self.y and player.pre_x == self.x):
            player.money += self.reward
            print(player.name, "nhận được {self.reward} khi đi qua ô Start!")

class Tile:
    def __init__(self,color,x,y,name,price):
        self.color=color
        self.x=x
        self.y=y
        self.name=name
        self.price=price

    def draw_down_small_tile(self):
        tile_surface = pygame.Surface((VERTICAL_TILE_SIZE_X, VERTICAL_TILE_SIZE_Y), pygame.SRCALPHA)
        tile_surface.fill(WHITE)

        pygame.draw.rect(tile_surface, self.color, (0, 0, VERTICAL_TILE_SIZE_X,20))
        pygame.draw.rect(tile_surface,BLACK,(0,0,VERTICAL_TILE_SIZE_X,VERTICAL_TILE_SIZE_Y),1)
        # Tạo font chữ
        font=pygame.font.Font(None,16)
        words = self.name.split()
        lines = []
        line = ""

        for word in words:
            test_line = line + " " + word if line else word
            if font.size(test_line)[0] <= VERTICAL_TILE_SIZE_X:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)

        y_offset = 0
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            tile_surface.blit(text_surface, ((VERTICAL_TILE_SIZE_X - text_surface.get_width()) // 2, y_offset+VERTICAL_TILE_SIZE_X))
            y_offset += font.get_height()

        screen.blit(tile_surface, (self.x, self.y))

    def draw_right_small_tile(self):
        tile_surface =pygame.Surface((HORIZONTAL_TILE_SIZE_X, HORIZONTAL_TILE_SIZE_Y), pygame.SRCALPHA) # Hỗ trợ trong suốt
        tile_surface.fill(WHITE)

        pygame.draw.rect(tile_surface, self.color, (0, 0, TILE_SIZE_ROW, 20))
        pygame.draw.rect(tile_surface, BLACK, (0, 0, HORIZONTAL_TILE_SIZE_X, HORIZONTAL_TILE_SIZE_Y), 1)

        # Tạo font chữ
        font = pygame.font.Font(None, 16)
        words = self.name.split()
        lines = []
        line = ""

        for word in words:
            test_line = line + " " + word if line else word
            if font.size(test_line)[0] <= HORIZONTAL_TILE_SIZE_X:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)

        y_offset = 0
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            tile_surface.blit(text_surface, ((HORIZONTAL_TILE_SIZE_X - text_surface.get_width()) // 2, y_offset + HORIZONTAL_TILE_SIZE_X))
            y_offset += font.get_height()

        tile_surface_right = pygame.transform.rotate(tile_surface, 90)
        screen.blit(tile_surface_right, (self.x, self.y))

    def draw_up_small_tile(self):
        tile_surface = pygame.Surface((VERTICAL_TILE_SIZE_X, VERTICAL_TILE_SIZE_Y), pygame.SRCALPHA)
        tile_surface.fill(WHITE)

        pygame.draw.rect(tile_surface, self.color, (0, 0, VERTICAL_TILE_SIZE_X, 20))
        pygame.draw.rect(tile_surface, BLACK, (0, 0, VERTICAL_TILE_SIZE_X, VERTICAL_TILE_SIZE_Y), 1)

        # Tạo font chữ
        font = pygame.font.Font(None, 16)
        words = self.name.split()
        lines = []
        line = ""

        for word in words:
            test_line = line + " " + word if line else word
            if font.size(test_line)[0] <= VERTICAL_TILE_SIZE_X:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)

        y_offset = 0
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            tile_surface.blit(text_surface, ((VERTICAL_TILE_SIZE_X - text_surface.get_width()) // 2, y_offset + VERTICAL_TILE_SIZE_X))
            y_offset += font.get_height()

        tile_surface_up = pygame.transform.rotate(tile_surface, 180)
        screen.blit(tile_surface_up, (self.x, self.y))

    def draw_left_small_tile(self):
        tile_surface = pygame.Surface((HORIZONTAL_TILE_SIZE_X, HORIZONTAL_TILE_SIZE_Y), pygame.SRCALPHA)
        tile_surface.fill(WHITE)
        pygame.draw.rect(tile_surface, self.color, (0, 0, HORIZONTAL_TILE_SIZE_X, 20))
        pygame.draw.rect(tile_surface, BLACK, (0, 0, HORIZONTAL_TILE_SIZE_X, HORIZONTAL_TILE_SIZE_Y), 1)

        # Tạo font chữ
        font = pygame.font.Font(None, 16)
        words = self.name.split()  # Tách từ
        lines = []
        line = ""

        for word in words:
            test_line = line + " " + word if line else word
            if font.size(test_line)[0] <= HORIZONTAL_TILE_SIZE_X:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)

        y_offset = 0
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            tile_surface.blit(text_surface, ((HORIZONTAL_TILE_SIZE_X - text_surface.get_width()) // 2, y_offset + HORIZONTAL_TILE_SIZE_X))
            y_offset += font.get_height()
        tile_surface_left=pygame.transform.rotate(tile_surface,270)
        screen.blit(tile_surface_left, (self.x, self.y))