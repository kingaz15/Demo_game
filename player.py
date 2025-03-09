import pygame
from Define import *
from Property import*
 
 
 #class property dùng để quản lí thông tin tài sản
 #class player quản lí thông tin người chơi và di chuyển, mua bán nhà, đi tù...
 
 
 
class Player:
    x = 0
    y = 0
    color = ""
 
    def __init__(self, name, player_number, index=0, money=50000000000000):
        self.index = index
        self.name = name
        self.player_number = player_number
        self.money = money
        self.owned_properties = []
        self.jail_status = False
        self.out_jail_card = False
        self.bankruptcy_status = False
 
 
     #kiểm tra tài sản hiện có
    def check_properties(self):
        for prop in self.owned_properties:
            print(f"\t{prop.get_name()}")
 
     # điều kiện để phá sản
    def is_bankrupt(self):
        total_val = self.money + sum(prop.get_value() for prop in self.owned_properties)
        if total_val <= 0:
            self.bankruptcy_status = True
        return total_val
 
 
     #kiểm tra thông tin người chơi, dùng điều kiên của bankrupt để hiện tổng số tiền đang có
    def check_status(self):
        print(f"Player Name: {self.name}")
        print(f"Player ID: {self.player_number}")
        print(f"Player Position: {self.index}")
        print(f"Wallet Amount: {self.money}")
        print("Properties Held: ", end="")
        if self.owned_properties:
            print(", ".join(prop.get_name() for prop in self.owned_properties))
        else:
            print("none")
        print(f"Total Net Worth: {self.is_bankrupt()}")
 
 
    def add_property(self, house):
        self.owned_properties.append(house)
        house.owner = self  # Cập nhật chủ sở hữu
        house.owned_flag = True  # Đánh dấu tài sản đã có người sở hữu
 
    def add_money(self, amount): #player1.add_money(200)
        self.money +=  amount
 
    def charge_money(self, charge): #player1.charge_money(100)
        self.money -= charge
 
    def pay_player(self, other, amount): #player1.pay_player(player2, 50)
        if self.money >= amount:
            self.money -= amount
            other.money += amount
        else:
            print(f"{self.name} không đủ tiền để thanh toán {amount} cho {other.name}!")
 
 
 
 
 
 
     #bán nhà
    def sell_property(self, prop_name):
        for prop in self.owned_properties:
            if prop.name == prop_name:
                self.money += prop.value
                prop.owner = None  # Xóa chủ sở hữu
                prop.owned_flag = False
                self.owned_properties.remove(prop) # Dùng __eq__ bên class property  để tìm và xóa
                return True
        return False
 
 
     # chuyển nhà cho player khác( chắc hàm này dùng cho phần change)
    def transfer_property(self, other, prop_name):
        for prop in self.owned_properties:
            if prop.name == prop_name:
                other.owned_properties.append(prop)
                self.owned_properties.remove(prop)
                return
 
    def go_to_jail(self):
         self.jail_status = True
         self.index = 10
 
 
 
 
 
 
    def move(self, steps):
         self.index = (self.index + steps) % TOTAL_TILES
 
    def draw_1(self):
        if self.index == 0:
            x = BIG_TILE_SIZE // 2
            y = BIG_TILE_SIZE // 2 + TILE_SIZE_ROW * NUM_VERTICAL_TILES_UP + 50
        elif self.index < NUM_VERTICAL_TILES_UP:
            x = TILE_SIZE_ROW // 2
            y = HEIGHT - (self.index + 1) * TILE_SIZE_ROW + TILE_SIZE_ROW // 2 - 15
        elif self.index <= NUM_VERTICAL_TILES_UP:
            x = BIG_TILE_SIZE // 2
            y = BIG_TILE_SIZE // 2
        elif self.index < NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT:
            x = (self.index - NUM_VERTICAL_TILES_UP + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 - 37
            y = TILE_SIZE_COLUMN // 2
        elif self.index <= NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT:
            x = BIG_TILE_SIZE // 2 + NUM_HORIZONTAL_TILES_RIGHT * TILE_SIZE_ROW + 60
            y = BIG_TILE_SIZE // 2
        elif self.index < NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN:
            x = WIDTH - TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 50
            y = (self.index - (NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT) + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 - 45
        elif self.index <= NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN:
             x = BIG_TILE_SIZE // 2 + NUM_HORIZONTAL_TILES_RIGHT * TILE_SIZE_ROW + 60
             y = BIG_TILE_SIZE // 2 + NUM_VERTICAL_TILES_DOWN * TILE_SIZE_COLUMN + 60
        else:
            x = WIDTH - (self.index - (NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN) + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 15
            y = HEIGHT - TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 20
 
        pygame.draw.circle(screen, RED, (x, y), PLAYER_RADIUS)
    def draw_2(self):
        if self.index == 0:
            x = BIG_TILE_SIZE // 2
            y = BIG_TILE_SIZE // 2 + TILE_SIZE_ROW * NUM_VERTICAL_TILES_UP + 50
        elif self.index < NUM_VERTICAL_TILES_UP:
            x = TILE_SIZE_ROW // 2
            y = HEIGHT - (self.index + 1) * TILE_SIZE_ROW + TILE_SIZE_ROW // 2 - 15
        elif self.index <= NUM_VERTICAL_TILES_UP:
            x = BIG_TILE_SIZE // 2
            y = BIG_TILE_SIZE // 2
        elif self.index < NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT:
            x = (self.index - NUM_VERTICAL_TILES_UP + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 - 37
            y = TILE_SIZE_COLUMN // 2
        elif self.index <= NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT:
            x = BIG_TILE_SIZE // 2 + NUM_HORIZONTAL_TILES_RIGHT * TILE_SIZE_ROW + 60
            y = BIG_TILE_SIZE // 2
        elif self.index < NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN:
            x = WIDTH - TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 50
            y = (self.index - (NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT) + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 - 45
        elif self.index <= NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN:
            x = BIG_TILE_SIZE // 2 + NUM_HORIZONTAL_TILES_RIGHT * TILE_SIZE_ROW + 60
            y = BIG_TILE_SIZE // 2 + NUM_VERTICAL_TILES_DOWN * TILE_SIZE_COLUMN + 60
        else:
            x = WIDTH - (self.index - (NUM_VERTICAL_TILES_UP + NUM_HORIZONTAL_TILES_RIGHT + NUM_VERTICAL_TILES_DOWN) + 1) * TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 15
            y = HEIGHT - TILE_SIZE_COLUMN + TILE_SIZE_COLUMN // 2 + 20
 
        pygame.draw.circle(screen, BLUE, (x, y), PLAYER_RADIUS)
