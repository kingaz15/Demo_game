import pygame
import sys
import random


from Define import *
from player import Player
from Tile import StartTile

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Monopoly game")
pygame.display.set_icon(pygame.image.load(PATH_IMAGE + "Monopoly.jpg"))
image_path = "Images/icon.png"
image = pygame.image.load(image_path)

image = pygame.transform.scale(image, (WIDTH_IMAGE, HEIGHT_IMAGE))
image_rect = image.get_rect(center = (WIDTH//2, HEIGHT//2))

# Initialize font
pygame.font.init()
font = pygame.font.SysFont(None, 55)

#Init Property
property1 = property("Mediterranean Avenue", 60, 2)

#Init Player
Player1 = Player(GREY, PLAYER_X, PLAYER_Y, "Player 1")
Start_Tile = StartTile()

#Main Loop
run = True
dice_value = 0 
text_dice = font.render(str(dice_value), True, BLACK)
money_text = font.render(f"Money: ${Player1.money}", True, BLACK)
while run:
    screen.fill(GREY)
    screen.blit(image, image_rect)
    
    #Monopoly Board
    pygame.draw.line(screen, WHITE, (1600,900), (1600, 0), 200)
    pygame.draw.line(screen, WHITE, (0, 900), (1600, 900), 200)
    pygame.draw.line(screen, WHITE, (0, 0), (0, 900), 200)
    pygame.draw.line(screen, WHITE, (0, 0), (1600, 0), 200)
    pygame.draw.rect(screen, BLACK, (0, 0, 150, 150))
    pygame.draw.rect(screen, BLACK, (0 , 750, 150, 150))
    pygame.draw.rect(screen, BLACK, (1450 , 750, 150, 150))
    pygame.draw.rect(screen, BLACK, (1450 , 0, 150, 150))
    pygame.draw.rect(screen, RED, (76 , 675, 25, 75))
    pygame.draw.rect(screen, RED, (76 , 600, 25, 75))
    pygame.draw.rect(screen, GREY, (76 , 375, 25, 75))
    pygame.draw.rect(screen, GREY, (76 , 300, 25, 75))
    pygame.draw.rect(screen, GREY, (76 , 150, 25, 75))
    pygame.draw.line(screen, BLACK, (100, 0), (100, 900), 3)
    pygame.draw.line(screen, BLACK, (0, 675), (100, 675), 3)
    pygame.draw.line(screen, BLACK, (0, 600), (100, 600), 3)
    pygame.draw.line(screen, BLACK, (0, 525), (100, 525), 3)
    pygame.draw.line(screen, BLACK, (0, 450), (100, 450), 3)
    pygame.draw.line(screen, BLACK, (0, 375), (100, 375), 3)
    pygame.draw.line(screen, BLACK, (0, 300), (100, 300), 3)
    pygame.draw.line(screen, BLACK, (0, 225), (100, 225), 3)
    pygame.draw.line(screen, BLACK, (75, 600), (75, 750), 3)
    pygame.draw.line(screen, BLACK, (0, 100), (1600, 100), 3)
    pygame.draw.line(screen, BLACK, (231.25, 0), (231.25, 100), 3)
    pygame.draw.line(screen, BLACK, (312.5, 0), (312.5, 100), 3)
    pygame.draw.line(screen, BLACK, (393.75, 0), (393.75, 100), 3)
    pygame.draw.line(screen, BLACK, (475, 0), (475, 100), 3)
    pygame.draw.line(screen, BLACK, (556.25, 0), (556.25, 100), 3)
    pygame.draw.line(screen, BLACK, (637.5, 0), (637.5, 100), 3)
    pygame.draw.line(screen, BLACK, (718.75, 0), (718.75, 100), 3)
    pygame.draw.line(screen, BLACK, (800, 0), (800, 100), 3)
    pygame.draw.line(screen, BLACK, (881.25, 0), (881.25, 100), 3)
    pygame.draw.line(screen, BLACK, (962.5, 0), (962.5, 100), 3)
    pygame.draw.line(screen, BLACK, (1043.75, 0), (1043.75, 100), 3)
    pygame.draw.line(screen, BLACK, (1125, 0), (1125, 100), 3)
    pygame.draw.line(screen, BLACK, (1206.25, 0), (1206.25, 100), 3)
    pygame.draw.line(screen, BLACK, (1287.5, 0), (1287.5, 100), 3)
    pygame.draw.line(screen, BLACK, (1368.75, 0), (1368.75, 100), 3)
    pygame.draw.line(screen, BLACK, (1450, 0), (1450, 100), 3)
    pygame.draw.line(screen, BLACK, (1500, 0), (1500, 900), 3)
    pygame.draw.line(screen, BLACK, (1600, 675), (1500, 675), 3)
    pygame.draw.line(screen, BLACK, (1600, 600), (1500, 600), 3)
    pygame.draw.line(screen, BLACK, (1600, 525), (1500, 525), 3)
    pygame.draw.line(screen, BLACK, (1600, 450), (1500, 450), 3)
    pygame.draw.line(screen, BLACK, (1600, 375), (1500, 375), 3)
    pygame.draw.line(screen, BLACK, (1600, 300), (1500, 300), 3)
    pygame.draw.line(screen, BLACK, (1600, 225), (1500, 225), 3)
    pygame.draw.line(screen, BLACK, (0, 800), (1600, 800), 3)
    pygame.draw.rect(screen, YELLOW, (0 , 755, 145, 145))
    pygame.draw.line(screen, BLACK, (231.25, 800), (231.25, 900), 3)
    pygame.draw.line(screen, BLACK, (312.5, 800), (312.5, 900), 3)
    pygame.draw.line(screen, BLACK, (393.75, 800), (393.75, 900), 3)
    pygame.draw.line(screen, BLACK, (475, 800), (475, 900), 3)
    pygame.draw.line(screen, BLACK, (556.25, 800), (556.25, 900), 3)
    pygame.draw.line(screen, BLACK, (637.5, 800), (637.5, 900), 3)
    pygame.draw.line(screen, BLACK, (718.75, 800), (718.75, 900), 3)
    pygame.draw.line(screen, BLACK, (800, 800), (800, 900), 3)
    pygame.draw.line(screen, BLACK, (881.25, 800), (881.25, 900), 3)
    pygame.draw.line(screen, BLACK, (962.5, 800), (962.5, 900), 3)
    pygame.draw.line(screen, BLACK, (1043.75,800), (1043.75, 900), 3)
    pygame.draw.line(screen, BLACK, (1125, 800), (1125, 900), 3)
    pygame.draw.line(screen, BLACK, (1206.25, 800), (1206.25, 900), 3)
    pygame.draw.line(screen, BLACK, (1287.5, 800), (1287.5, 900), 3)
    pygame.draw.line(screen, BLACK, (1368.75, 800), (1368.75, 900), 3)
    pygame.draw.line(screen, BLACK, (1450, 800), (1450, 900), 3)
    Player1.show(screen)

    screen.blit(text_dice, (400, 500))
    screen.blit(money_text, (280, 200))
    #Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_value = random.randint(1, 6)
                PLAYER_MOVE = dice_value * 75
                text_dice = font.render(str(dice_value), True, BLACK)
                Player1.move(dice_value)
                Start_Tile.pass_though(Player1)
                money_text = font.render(f"Money: ${Player1.money}", True, BLACK)
                print(dice_value)

    pygame.display.flip()



pygame.quit()
sys.exit()