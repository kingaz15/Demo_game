import pygame.transform
from pygame import SRCALPHA
from pygame.examples.midi import NullKey

from player import Player
from Define import *

class Tile:
    def __init__(self, color, x, y, name, price,img):
        self.color = color
        self.x = x
        self.y = y
        self.name = name
        self.price = price
        self.img=img

    def draw(self, width, height, rotation=0):
        tile_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        tile_surface.fill(WHITE)

        pygame.draw.rect(tile_surface, self.color, (0, 0, width, 20))
        pygame.draw.rect(tile_surface, BLACK, (0, 0, width, height), 1)

        if(self.img):
            used_img=pygame.transform.scale(self.img,(50,50))
            tile_surface.blit(self.img,(width/2-25,30))


        font = pygame.font.Font(None, 16)
        words = self.name.split()
        lines = []
        line = ""

        for word in words:
            test_line = line + " " + word if line else word
            if font.size(test_line)[0] <= width:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)

        y_offset = 0
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            tile_surface.blit(text_surface, ((width - text_surface.get_width()) // 2, y_offset + width))
            y_offset += font.get_height()

        if rotation != 0:
            tile_surface = pygame.transform.rotate(tile_surface, rotation)

        screen.blit(tile_surface, (self.x, self.y))

class Small_tile(Tile):
    def __init__(self, color, x, y, name, price):
        super().__init__(color, x, y, name, price,None)

    def draw_down_tile(self):
        self.draw(VERTICAL_TILE_SIZE_X, VERTICAL_TILE_SIZE_Y, rotation=0)
    def draw_up_tile(self):
        self.draw(VERTICAL_TILE_SIZE_X, VERTICAL_TILE_SIZE_Y, rotation=180)
    def draw_right_tile(self):
        self.draw(HORIZONTAL_TILE_SIZE_X, HORIZONTAL_TILE_SIZE_Y, rotation=90)
    def draw_left_tile(self):
        self.draw(HORIZONTAL_TILE_SIZE_X, HORIZONTAL_TILE_SIZE_Y, rotation=270)



class BigTile(Tile):
    def __init__(self, x, y, name,img):
        super().__init__(None, x, y, name,0,img)

    def draw_big_tile(self,width,height,rotation):
        # Main tile surface (not rotated)
        tile_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        tile_surface.fill(WHITE)
        pygame.draw.rect(tile_surface, BLACK, (0, 0, width, height), 1)

        # Create content surface
        content = pygame.Surface((width, height), pygame.SRCALPHA)

        # Add text
        font = pygame.font.Font(None, 30)
        words = self.name.split()
        lines = []
        line = ""

        for word in words:
            test_line = line + " " + word if line else word
            if font.size(test_line)[0] <= width:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)

        y_offset = 40
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            content.blit(text_surface, ((width - text_surface.get_width()) // 2, y_offset))
            y_offset += font.get_height()

        # Add image
        newimg = pygame.transform.scale(self.img, (50, 50))
        content.blit(newimg, ((width - 50) // 2, y_offset + 5))

        # Rotate only the content
        rotated_content = pygame.transform.rotate(content, rotation)

        # Calculate position to center rotated content inside tile
        rot_w, rot_h = rotated_content.get_size()
        tile_surface.blit(rotated_content, ((width - rot_w) // 2, (height - rot_h) // 2))

        # Finally blit the tile to screen
        screen.blit(tile_surface, (self.x, self.y))

class Special_Tile(Tile):
    def __init__(self,x,y,name,img):
        super().__init__(WHITE,x,y,name,0,img)

    def draw_up_special_tile(self):
        self.draw(VERTICAL_TILE_SIZE_X,VERTICAL_TILE_SIZE_Y,180)

    def draw_down_special_tile(self):
        self.draw(VERTICAL_TILE_SIZE_X,VERTICAL_TILE_SIZE_Y,0)

    def draw_right_special_tile(self):
        self.draw(VERTICAL_TILE_SIZE_X,VERTICAL_TILE_SIZE_Y,90)

    def draw_left_special_tile(self):
        self.draw(VERTICAL_TILE_SIZE_X,VERTICAL_TILE_SIZE_Y,270)










