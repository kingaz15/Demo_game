from player import Player

class StartTile:
    def __init__(self, x = 50, y = 650):

        self.x = x
        self.y = y
        self.reward = 200
    
    def pass_though(self, player):
        if (player.pre_x > self.x and player.x <= self.x and player.pre_y == self.y) or(player.pre_y < self.y and player.y >= self.y and player.pre_x == self.x):
            player.money += self.reward
            print(player.name, "nhận được {self.reward} khi đi qua ô Start!")