
import pygame
import sys
import random

from Define import *
from Player import *
from Main_Board import draw_board
from Property import*

pygame.display.set_caption("Monopoly game")
pygame.display.set_icon(pygame.image.load(PATH_IMAGE + "Monopoly.jpg"))
image_path = "Images/icon.png"
image = pygame.image.load(image_path)

image = pygame.transform.scale(image, (WIDTH_IMAGE, HEIGHT_IMAGE))
image_rect = image.get_rect(center = (WIDTH//2, HEIGHT//2))

# Initialize font
pygame.font.init()
font = pygame.font.SysFont(None, 55)

# Init Property
properties = [
    Property(1, "brown", 5000, "Seoul"),
    Property(2, "brown", 5000, "Busan"),
    Property(3, "brown", 5000, "CHANCE"),
    Property(4, "brown", 5000, "Ha Noi"),
    Property(5, "brown", 5000, "Ho Chi Minh City"),
    Property(6, "brown", 5000, "Bangkok"),
    Property(7, "brown", 5000, "London"),
    Property(8, "brown", 5000, "Dubai"),
    Property(9, "brown", 5000, "Sydney"),
    Property(10, "brown", 5000, "SPEACIAL"),
    Property(11, "brown", 5000, "Chicago"),
    Property(12, "brown", 5000, "Las Vegas"),
    Property(13, "brown", 5000, "New York"),
    Property(14, "brown", 5000, "TAX"),
    Property(15, "brown", 5000, "Lyon"),
    Property(16, "brown", 5000, "Paris"),
    Property(17, "brown", 5000, "CHANCE"),
    Property(18, "brown", 5000, "Osaka"),
    Property(19, "brown", 5000, "Tokyo"),
    Property(20, "brown", 5000, "Granada"),
    Property(21, "brown", 5000, "Seville"),
    Property(22, "brown", 5000, "Madrid"),
    Property(23, "brown", 5000, "Bali Beach"),
    Property(24, "brown", 5000, "HongKong"),
    Property(25, "brown", 5000, "Beijing"),
    Property(26, "brown", 5000, "Bandung"),
    Property(27, "brown", 5000, "Jakarta"),
    Property(28, "brown", 5000, "Ahmedabad"),
    Property(29, "brown", 5000, "Delhi"),
    Property(30, "brown", 5000, "Mumbai"),
    Property(31, "brown", 5000, "Berlin"),
    Property(32, "brown", 5000, "Cyprus"),
    Property(33, "brown", 5000, "Hamburg"),
    Property(34, "brown", 5000, "CHANCE"),
    Property(35, "brown", 5000, "Rome"),
    Property(36, "brown", 5000, "Milan"),
    Property(37, "brown", 5000, "Venice"),
    Property(38, "brown", 5000, "Shanghai"),

]

# Init Player
Player1 = Player("Hoan", 1)
Player2 = Player("An", 2)


buying = False

# Main Loop
run = True
dice_1, dice_2 = 1 ,1
money_text = font.render(f"Money: ${Player1.money}", True, BLACK)
clock = pygame.time.Clock()


def show_message(text, delay=2000):
    pygame.font.init()
    message_font = pygame.font.SysFont("Arial", 40)
    msg_bg = pygame.Rect(WIDTH//2 - 500, HEIGHT//2 - 100, 400, 200)
    pygame.draw.rect(screen, WHITE, msg_bg)
    pygame.draw.rect(screen, BLACK, msg_bg, 3)
    text_surface = message_font.render(text, True, BLACK)
    screen.blit(text_surface, (msg_bg.x + 20, msg_bg.y + 70))
    pygame.display.update()
    pygame.time.delay(500)


def draw_button(screen, rect, color, text, hover_color=None,):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    is_hovered = rect.collidepoint(mouse_x, mouse_y)
    button_color = hover_color if is_hovered and hover_color else color
    shadow_rect = rect.move(3, 3)  # Dịch xuống 3px để tạo bóng
    pygame.draw.rect(screen, GREY, shadow_rect, border_radius=10)
    pygame.draw.rect(screen, button_color, rect, border_radius=10)
    button_font = pygame.font.SysFont("Arial", 40)
    text_surface = button_font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def show_purchase_menu(property, player):
    menu_font = pygame.font.SysFont(None, 45)
    menu_bg = pygame.Rect(WIDTH//2 - 200, HEIGHT//2 - 150, 400, 300)
    pygame.draw.rect(screen, GREY, menu_bg, border_radius=10)
    pygame.draw.rect(screen, BLACK, menu_bg, 3, border_radius=10)
    text_title = menu_font.render(f"Mua {property.name} ?", True, BLACK)
    text_price = menu_font.render(f"Gia: ${property.value}", True, BLACK)
    buy_button = pygame.Rect(WIDTH // 2 - 140, HEIGHT // 2 + 50, 120, 50)
    skip_button = pygame.Rect(WIDTH // 2 + 20, HEIGHT // 2 + 50, 120, 50)
    draw_button(screen, buy_button, GREEN, "Mua", hover_color=(0, 200, 0))
    draw_button(screen, skip_button, RED, "Bo qua", hover_color=(200, 0, 0))
    text_buy = menu_font.render("Mua", True, BLACK)
    text_skip = menu_font.render("Bo qua", True, BLACK)
    screen.blit(text_title, (menu_bg.x + 50, menu_bg.y + 20))
    screen.blit(text_price, (menu_bg.x + 50, menu_bg.y + 50))
    screen.blit(text_buy, (menu_bg.x + 50, menu_bg.y + 90))
    screen.blit(text_skip, (menu_bg.x + 50, menu_bg.y + 120))
    pygame.display.update()
    pygame.time.delay(2000)

    return buy_button, skip_button

selected_property = None

while run:
    screen.fill(WHITE)
    screen.blit(image, image_rect)
    draw_board()
    Player1.draw()


    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:  # Xử lý phím bấm
            if event.key == pygame.K_ESCAPE:
                run = False

            elif event.key == pygame.K_SPACE:
                dice_1, dice_2 = roll_dice()
                Player1.move(dice_1 + dice_2)
                pygame.display.update()  # Cập nhật màn hình sau khi roll xúc xắc

                # Kiểm tra ô hiện tại của người chơi
                current_position = Player1.index
                print(f"{Player1.name} đang đứng ở ô {current_position}")
                for prop in properties:
                    if prop.id == current_position:
                        print(f"Người chơi đã đến ô tài sản: {prop.name}")

                        if not prop.owned_flag:  # Nếu chưa có chủ
                            print("Hiển thị bảng mua nhà")
                            buy_button, skip_button = show_purchase_menu(prop, Player1)  # Lưu lại nút để xử lý click
                            selected_property = prop

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Kiểm tra click chuột
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Lấy tọa độ chuột
            if selected_property is not None and skip_button is not None:
             if buy_button and buy_button.collidepoint(mouse_x, mouse_y):
                if Player1.money >= selected_property.value:
                    Player1.charge_money(selected_property.value)
                    Player1.add_property(selected_property)
                    selected_property.owner = Player1
                    selected_property.owned_flag = True
                    show_message(f"{Player1.name} da mua {selected_property.name} voi gia {selected_property.value}!")
                else:
                    show_message("Khong du tien mua")
                selected_property = None
                buy_button, skip_button = None, None  # Xóa nút sau khi xử lý xong (thụt lề đúng)

             elif skip_button.collidepoint(mouse_x, mouse_y):
                    show_message("Nguoi choi tu choi mua")
                    selected_property = None  # Xóa tài sản sau khi từ chối
                    buy_button, skip_button = None, None  # Xóa nút sau khi xử lý xong

    pygame.display.flip()
    clock.tick (60)


pygame.quit()
sys.exit()
