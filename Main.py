import pygame
import random


from Define import *
from player import Player
from Tile import StartTile

screen = pygame.display.set_mode((WiDTH, HEiTDH))
pygame.display.set_caption("Monopoly game")
pygame.display.set_icon(pygame.image.load(PATH_IMAGE + "Monopoly.jpg"))
image_path = "Images/icon.png"
image = pygame.image.load(image_path)

image = pygame.transform.scale(image, (WIDTH_IMAGE, HEIGHT_IMAGE))
image_rect = image.get_rect(center = (WiDTH//2, HEiTDH//2))

# Initialize font
pygame.font.init()
font = pygame.font.SysFont(None, 55)

#Init Property
property1 = property("Mediterranean Avenue", 60, 2)

#Init Player
Player1 = Player(BLACK, PLAYER_X, PLAYER_Y, "Player 1")
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
    pygame.draw.line(screen, WHITE, (800,700), (800, 0), 200)
    pygame.draw.line(screen, WHITE, (0, 700), (800, 700), 200)
    pygame.draw.line(screen, WHITE, (0, 0), (0, 700), 200)
    pygame.draw.line(screen, WHITE, (0, 0), (800, 0), 200)
    pygame.draw.rect(screen, YELLOW, (705.5, 605.5, 90, 90))
    pygame.draw.rect(screen, YELLOW, (605.5, 605.5, 90, 90))
    pygame.draw.rect(screen, YELLOW, (505.5, 605.5, 90, 90))
    pygame.draw.rect(screen, CYAN, (405.5, 605.5, 90, 90)) 
    pygame.draw.rect(screen, CYAN, (305.5, 605.5, 90, 90))
    pygame.draw.rect(screen, BLUE, (205.5, 605.5, 90, 90))
    pygame.draw.rect(screen, BLUE, (105.5, 605.5, 90, 90))
    pygame.draw.rect(screen, PURPLE, (5.5, 605.5, 90, 90))
    pygame.draw.rect(screen, RED, (5.5, 505.5, 90, 90))
    pygame.draw.rect(screen, RED, (5.5, 405.5, 90, 90))
    pygame.draw.rect(screen, RED, (5.5, 305.5, 90, 90))
    pygame.draw.rect(screen, GREY, (5.5, 205.5, 90, 90))
    pygame.draw.rect(screen, GREY, (5.5, 105.5, 90, 90))
    pygame.draw.rect(screen, GREY, (5.5, 5.5, 90, 90))
    pygame.draw.rect(screen, GREEN, (105.5, 5.5, 90, 90))
    pygame.draw.rect(screen, GREEN, (205.5, 5.5, 90, 90))
    pygame.draw.rect(screen, GREEN, (305.5, 5.5, 90, 90))
    pygame.draw.rect(screen, PINK, (405.5, 5.5, 90, 90))
    pygame.draw.rect(screen, PINK, (505.5, 5.5, 90, 90))
    pygame.draw.rect(screen, PINK, (605.5, 5.5, 90, 90))
    pygame.draw.rect(screen, ORGANGE, (705.5, 5.5, 90, 90))
    pygame.draw.rect(screen, ORGANGE, (705.5, 105.5, 90, 90))
    pygame.draw.rect(screen, ORGANGE, (705.5, 205.5, 90, 90))
    pygame.draw.rect(screen, BROWN, (705.5, 305.5, 90, 90))
    pygame.draw.rect(screen, BROWN, (705.5, 405.5, 90, 90))
    pygame.draw.rect(screen, BROWN, (705.5, 505.5, 90, 90))

    #Player
    Player1.show(screen)

    screen.blit(text_dice, (400, 500))
    screen.blit(money_text, (280, 200))
    #Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_value = random.randint(1, 6)
                PLAYER_MOVE = dice_value * 100
                text_dice = font.render(str(dice_value), True, BLACK)
                Player1.move(dice_value)
                Start_Tile.pass_though(Player1)
                money_text = font.render(f"Money: ${Player1.money}", True, BLACK)
                print(dice_value)

    pygame.display.flip()



pygame.quit()