import pygame
from tile import *


def draw_board():
    screen.fill(GREY)

    # for i in range(NUM_VERTICAL_TILES_UP):
    #     if i == 0:
    #         x = 0
    #         y = HEIGHT - (i + 1) * BIG_TILE_SIZE + 35
    #         pygame.draw.rect(screen, BLACK, (x, y, BIG_TILE_SIZE + 5, BIG_TILE_SIZE), 2)
    #     else:
    #         x = 0
    #         y = HEIGHT - (i + 1) * TILE_SIZE_COLUMN - 13
    #         pygame.draw.rect(screen, BLACK, (x, y, 130, TILE_SIZE_COLUMN), 2)
    #
    # for i in range(NUM_HORIZONTAL_TILES_RIGHT):
    #     if i == 0:
    #         x = (i) * BIG_TILE_SIZE
    #         y = 0
    #         pygame.draw.rect(screen, BLACK, (x, y, BIG_TILE_SIZE, BIG_TILE_SIZE + 8), 2)
    #     else:
    #         x = (i + 1) * TILE_SIZE_ROW - 50
    #         y = 0
    #         pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE_ROW, 130), 2)
    #
    # for i in range(NUM_VERTICAL_TILES_DOWN):
    #     if i == 0:
    #         x = WIDTH - BIG_TILE_SIZE + 64
    #         y = (i) * TILE_SIZE_COLUMN
    #         pygame.draw.rect(screen, BLACK, (x, y, BIG_TILE_SIZE + 7, BIG_TILE_SIZE), 2)
    #     else:
    #         x = WIDTH - TILE_SIZE_COLUMN + 28
    #         y = (i + 1) * TILE_SIZE_COLUMN - 50
    #         pygame.draw.rect(screen, BLACK, (x, y, 145, TILE_SIZE_COLUMN), 2)
    #
    # for i in range(NUM_HORIZONTAL_TILES_LEFT):
    #     if i == 0:
    #         x = 1450
    #         y = 742
    #         pygame.draw.rect(screen, BLACK, (x, y, BIG_TILE_SIZE + 2, BIG_TILE_SIZE + 7), 2)
    #     else:
    #         x = WIDTH - (i + 1) * TILE_SIZE_ROW + 15
    #         y = HEIGHT - TILE_SIZE_ROW
    #         pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE_ROW, 140), 2)

    # top tile
    block1=Tile((191,165,178),150,0,"LONDON",5000)
    block1.draw_up_small_tile()
    block2 = Tile((191 ,165,178), 150+VERTICAL_TILE_SIZE_X*1, 0, "DUBAI", 5000)
    block2.draw_up_small_tile()
    block3 = Tile((191,165,178), 150+VERTICAL_TILE_SIZE_X*2, 0, "SYDNEY", 5000)
    block3.draw_up_small_tile()
    block4 = Tile((191,165,178), 150+VERTICAL_TILE_SIZE_X*3, 0, "SPECIAL",5000)
    block4.draw_up_small_tile()
    block5 = Tile((196,210,210), 150+VERTICAL_TILE_SIZE_X*4, 0, "CHICAGO", 5000)
    block5.draw_up_small_tile()
    block6 = Tile((196,210,210), 150+VERTICAL_TILE_SIZE_X*5, 0, "LAS VEGAS", 5000)
    block6.draw_up_small_tile()
    block7 = Tile((196,210,210), 150+VERTICAL_TILE_SIZE_X*6, 0, "NEW YORK", 5000)
    block7.draw_up_small_tile()
    block8 = Tile((191,165,178), 150+VERTICAL_TILE_SIZE_X*7, 0, "TAX", 5000)
    block8.draw_up_small_tile()
    block9 = Tile((176 ,172, 197), 150+VERTICAL_TILE_SIZE_X*8, 0, "LYON", 5000)
    block9.draw_up_small_tile()
    block10 = Tile((176 ,172, 197), 150+VERTICAL_TILE_SIZE_X*9, 0, "PARIS", 5000)
    block10.draw_up_small_tile()
    block11 = Tile((176 ,172, 197), 150+VERTICAL_TILE_SIZE_X*10, 0, "CHANCE", 5000)
    block11.draw_up_small_tile()
    block12 = Tile((229,174,171), 150+VERTICAL_TILE_SIZE_X*11, 0, "OSAKE", 5000)
    block12.draw_up_small_tile()
    block13 = Tile((229, 174, 171), 150+VERTICAL_TILE_SIZE_X*12, 0, "TOKYO", 5000)
    block13.draw_up_small_tile()



    #right tile
    block14 = Tile((205,182,150), (WIDTH-HORIZONTAL_TILE_SIZE_X+36), 150, "GRANA", 5000)
    block14.draw_right_small_tile()
    block15 = Tile((205,182,150), (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X, "SEVILLE", 5000)
    block15.draw_right_small_tile()
    block16 = Tile((205,182,150), (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X*2, "MADRID", 5000)
    block16.draw_right_small_tile()
    block17 = Tile(GREEN, (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X*3, "BALI BEACH", 5000)
    block17.draw_right_small_tile()
    block18 = Tile((222 ,214, 193), (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X*4, "HONG KONG", 5000)
    block18.draw_right_small_tile()
    block19 = Tile((222 ,214, 193), (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X*5, "BEIJING", 5000)
    block19.draw_right_small_tile()

    #bottom tile
    block20 = Tile((222 ,214, 193), 150, ((HEIGHT-VERTICAL_TILE_SIZE_Y)+36), "SHANGHAI", 5000)
    block20.draw_down_small_tile()
    block21 = Tile((200 ,223, 109), 150+VERTICAL_TILE_SIZE_X*1, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "VENICE", 5000)
    block21.draw_down_small_tile()
    block22 = Tile((200 ,223, 109), 150+VERTICAL_TILE_SIZE_X*2, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MILAN", 5000)
    block22.draw_down_small_tile()
    block23 = Tile((200 ,223, 109), 150+VERTICAL_TILE_SIZE_X*3, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "ROME", 5000)
    block23.draw_down_small_tile()
    block24 = Tile(ORANGE, 150+VERTICAL_TILE_SIZE_X*4, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "CHANCE", 5000)
    block24.draw_down_small_tile()
    block25 = Tile((215,215,155), 150+VERTICAL_TILE_SIZE_X*5, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "HAMBURG", 5000)
    block25.draw_down_small_tile()
    block26 = Tile((215,215,155), 150+VERTICAL_TILE_SIZE_X*6, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "CYPRUS", 5000)
    block26.draw_down_small_tile()
    block27 = Tile((215,215,155), 150+VERTICAL_TILE_SIZE_X*7, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "BERLIN", 5000)
    block27.draw_down_small_tile()
    block28 = Tile(WHITE, 150+VERTICAL_TILE_SIZE_X*8, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block28.draw_down_small_tile()
    block29 = Tile(WHITE, 150+VERTICAL_TILE_SIZE_X*9, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block29.draw_down_small_tile()
    block30 = Tile(WHITE, 150+VERTICAL_TILE_SIZE_X*10, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block30.draw_down_small_tile()
    block31 = Tile(WHITE, 150+VERTICAL_TILE_SIZE_X*11, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block31.draw_down_small_tile()
    block32 = Tile(WHITE, 150+VERTICAL_TILE_SIZE_X*12, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block32.draw_down_small_tile()

    #left tile
    block33 = Tile(WHITE, 0, 150, "MY HOUSE", 5000)
    block33.draw_left_small_tile()
    block34 = Tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*1, "MY HOUSE", 5000)
    block34.draw_left_small_tile()
    block35 = Tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*2, "MY HOUSE", 5000)
    block35.draw_left_small_tile()
    block36 = Tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*3, "MY HOUSE", 5000)
    block36.draw_left_small_tile()
    block37 = Tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*4, "MY HOUSE", 5000)
    block37.draw_left_small_tile()
    block38 = Tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*5, "MY HOUSE", 5000)
    block38.draw_left_small_tile()

    #dice


