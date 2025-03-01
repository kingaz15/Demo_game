from player import Player

class StartTile:
    def __init__(self, x = 50, y = 650):
        """
        Khởi tạo ô Start
        :param x: Tọa độ x của ô Start
        :param y: Tọa độ y của ô Start
        :param reward: Số tiền thưởng khi đi qua ô Start
        """
        self.x = x
        self.y = y
        self.reward = 200
    
    def pass_through(self, Player):
            if Player.x < 50 and Player.y > 650:
                Player.money += self.reward
                print(Player.name, "nhận được {self.reward} khi đi qua ô Start!")