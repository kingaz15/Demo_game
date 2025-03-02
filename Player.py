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
        self.pre_x = x
        self.pre_y = y

    def show(self, surface):
        pygame.draw.circle( surface, self.color, (self.x, self.y), PLAYER_RADIUS)


    def move(self, dice_value):
        self.pre_x = self.x
        self.pre_y = self.y
        print(self.x, self.y)
        if self.x == 20 or self.y == 20:
            self.y -= dice_value * 75
            if self.y < 0:
                self.x += -self.y + 60
                self.y = 20
                if self.x == 20 and 50 <= self.y <= 125:
                    self.x += -self.y + 75*3
                    self.y = 20
                    print(self.x, self.y)
                if self.x > 1600:
                    self.y += self.x - 1550
                    self.x = 1550
        elif self.x == 1550 or self.y == 850:
            self.y += dice_value * 75 
            if self.y > 900:
                self.x -= self.y - 850
                self.y = 850
            if self.x < 0:
                self.y -= -self.x + 75
                self.x = 20

class property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None