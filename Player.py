import pygame
from Define import *

class Player:
    x=0
    y=0
    color=""
    
    def __init__(self, color, x, y, name, money = 1500):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.money = money


    def show(self, surface):
        pygame.draw.circle( surface, self.color, (self.x, self.y), PLAYER_RADIUS)


    def move(self, dice_value):
        if self.x == 50 or self.y == 50:
            self.y -= dice_value * 100
            if self.y < 0:
                self.x += -self.y + 50
                self.y = 50
            if self.x > 800:
                self.y += self.x - 750
                self.x = 750
        elif self.x == 750 or self.y == 650:
            self.y += dice_value * 100 
            if self.y > 700:
                self.x -= self.y - 650
                self.y = 650
            if self.x < 0:
                self.y -= -self.x + 50
                self.x = 50

class property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None