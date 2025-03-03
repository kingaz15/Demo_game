import pygame
import sys
import random

from Define import *
from player import Player
from Main_Board import draw_board

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
Player1 = Player()

#Main Loop
run = True
dice_1, dice_2 = 1,1
money_text = font.render(f"Money: ${Player1.money}", True, BLACK)
clock = pygame.time.Clock()
while run:
    screen.fill(WHITE)
    screen.blit(image, image_rect)
    draw_board()
    Player1.draw()
    

    text_dice = font.render(f"Dice: {dice_1} + {dice_2} = {dice_1 + dice_2}", True, BLACK)
    screen.blit(text_dice, (WIDTH // 2 - 550, 550))
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
                dice_1, dice_2 = roll_dice()
                Player1.move(dice_1 + dice_2)
                money_text = font.render(f"Money: ${Player1.money}", True, BLACK)
            

    pygame.display.flip()
    clock.tick (60)


pygame.quit()
sys.exit()