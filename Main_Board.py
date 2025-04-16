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
    block1=Small_tile((191,165,178),150,0,"LONDON",5000)
    block1.draw_up_tile()
    block2 = Small_tile((191 ,165,178), 150+VERTICAL_TILE_SIZE_X*1, 0, "DUBAI", 5000)
    block2.draw_up_tile()
    block3 = Small_tile((191,165,178), 150+VERTICAL_TILE_SIZE_X*2, 0, "SYDNEY", 5000)
    block3.draw_up_tile()
    block4 = Small_tile((191,165,178), 150+VERTICAL_TILE_SIZE_X*3, 0, "SPECIAL",5000)
    block4.draw_up_tile()
    block5 = Small_tile((196,210,210), 150+VERTICAL_TILE_SIZE_X*4, 0, "CHICAGO", 5000)
    block5.draw_up_tile()
    block6 = Small_tile((196,210,210), 150+VERTICAL_TILE_SIZE_X*5, 0, "LAS VEGAS", 5000)
    block6.draw_up_tile()
    block7 = Small_tile((196,210,210), 150+VERTICAL_TILE_SIZE_X*6, 0, "NEW YORK", 5000)
    block7.draw_up_tile()
    block8 = Small_tile((191,165,178), 150+VERTICAL_TILE_SIZE_X*7, 0, "TAX", 5000)
    block8.draw_up_tile()
    block9 = Small_tile((176 ,172, 197), 150+VERTICAL_TILE_SIZE_X*8, 0, "LYON", 5000)
    block9.draw_up_tile()
    block10 = Small_tile((176 ,172, 197), 150+VERTICAL_TILE_SIZE_X*9, 0, "PARIS", 5000)
    block10.draw_up_tile()
    block11 = Small_tile((176 ,172, 197), 150+VERTICAL_TILE_SIZE_X*10, 0, "CHANCE", 5000)
    block11.draw_up_tile()
    block12 = Small_tile((229,174,171), 150+VERTICAL_TILE_SIZE_X*11, 0, "OSAKE", 5000)
    block12.draw_up_tile()
    block13 = Small_tile((229, 174, 171), 150+VERTICAL_TILE_SIZE_X*12, 0, "TOKYO", 5000)
    block13.draw_up_tile()



    #right tile
    block14 = Small_tile((205,182,150), (WIDTH-HORIZONTAL_TILE_SIZE_X+36), 150, "GRANA", 5000)
    block14.draw_right_tile()
    block15 = Small_tile((205,182,150), (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X, "SEVILLE", 5000)
    block15.draw_right_tile()
    block16 = Small_tile((205,182,150), (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X*2, "MADRID", 5000)
    block16.draw_right_tile()
    block17 = Small_tile(GREEN, (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X*3, "BALI BEACH", 5000)
    block17.draw_right_tile()
    block18 = Small_tile((222 ,214, 193), (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X*4, "HONG KONG", 5000)
    block18.draw_right_tile()
    block19 = Small_tile((222 ,214, 193), (WIDTH - HORIZONTAL_TILE_SIZE_X + 36), 150+HORIZONTAL_TILE_SIZE_X*5, "BEIJING", 5000)
    block19.draw_right_tile()

    #bottom tile
    block20 = Small_tile((222 ,214, 193), 150, ((HEIGHT-VERTICAL_TILE_SIZE_Y)+36), "SHANGHAI", 5000)
    block20.draw_down_tile()
    block21 = Small_tile((200 ,223, 109), 150+VERTICAL_TILE_SIZE_X*1, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "VENICE", 5000)
    block21.draw_down_tile()
    block22 = Small_tile((200 ,223, 109), 150+VERTICAL_TILE_SIZE_X*2, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MILAN", 5000)
    block22.draw_down_tile()
    block23 = Small_tile((200 ,223, 109), 150+VERTICAL_TILE_SIZE_X*3, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "ROME", 5000)
    block23.draw_down_tile()
    block24 = Small_tile(ORANGE, 150+VERTICAL_TILE_SIZE_X*4, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "CHANCE", 5000)
    block24.draw_down_tile()
    block25 = Small_tile((215,215,155), 150+VERTICAL_TILE_SIZE_X*5, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "HAMBURG", 5000)
    block25.draw_down_tile()
    block26 = Small_tile((215,215,155), 150+VERTICAL_TILE_SIZE_X*6, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "CYPRUS", 5000)
    block26.draw_down_tile()
    block27 = Small_tile((215,215,155), 150+VERTICAL_TILE_SIZE_X*7, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "BERLIN", 5000)
    block27.draw_down_tile()
    block28 = Small_tile(WHITE, 150+VERTICAL_TILE_SIZE_X*8, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block28.draw_down_tile()
    block29 = Small_tile(WHITE, 150+VERTICAL_TILE_SIZE_X*9, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block29.draw_down_tile()
    block30 = Small_tile(WHITE, 150+VERTICAL_TILE_SIZE_X*10, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block30.draw_down_tile()
    block31 = Small_tile(WHITE, 150+VERTICAL_TILE_SIZE_X*11, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block31.draw_down_tile()
    block32 = Small_tile(WHITE, 150+VERTICAL_TILE_SIZE_X*12, ((HEIGHT - VERTICAL_TILE_SIZE_Y) + 36), "MY HOUSE", 5000)
    block32.draw_down_tile()

    #left tile
    block33 = Small_tile(WHITE, 0, 150, "MY HOUSE", 5000)
    block33.draw_left_tile()
    block34 = Small_tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*1, "MY HOUSE", 5000)
    block34.draw_left_tile()
    block35 = Small_tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*2, "MY HOUSE", 5000)
    block35.draw_left_tile()
    block36 = Special_Tile(0, 150+HORIZONTAL_TILE_SIZE_X*3, "CHANCE", dice_face1)
    block36.draw_left_special_tile()
    block37 = Small_tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*4, "MY HOUSE", 5000)
    block37.draw_left_tile()
    block38 = Small_tile(WHITE, 0, 150+HORIZONTAL_TILE_SIZE_X*5, "MY HOUSE", 5000)
    block38.draw_left_tile()

    # BIG TILE
    Start=BigTile(0,0,"START",dice_face1)
    Start.draw_big_tile(BIG_TILE_SIZE,BIG_TILE_SIZE,225)
    visit=BigTile((WIDTH-BIG_TILE_SIZE+65),0,"VISIT",dice_face5)
    visit.draw_big_tile(BIG_TILE_SIZE,BIG_TILE_SIZE,135)
    prison=BigTile(0,HEIGHT-BIG_TILE_SIZE+36,"PRISON",dice_face3)
    prison.draw_big_tile(BIG_TILE_SIZE,BIG_TILE_SIZE,315)
    vacation = BigTile(WIDTH-BIG_TILE_SIZE+65, HEIGHT - BIG_TILE_SIZE + 36, "PRISON", dice_face3)
    vacation.draw_big_tile(BIG_TILE_SIZE,BIG_TILE_SIZE,45)




