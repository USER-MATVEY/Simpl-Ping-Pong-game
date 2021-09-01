import pygame
from pygame import *

FPS = 60
Color = (127, 255, 0)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, start_x, start_y, sprite_hight, sprite_weight, hp, sprite_class):
        super().__init__()
        self.sprite_class = sprite_class
        self.HP = hp
        self.sprite_hight = sprite_hight
        self.sprite_weight = sprite_weight
        self.image = transform.scale(image.load(player_image), (self.sprite_hight, self.sprite_weight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.flag = True

    def show_sprite(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(sprite.Sprite):
    def __init__(self, color, width, height, rect_x, rect_y, speed, K_Up, K_Down):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed
        self.key_up = K_Up
        self.key_down = K_Down

    def move_player(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[self.key_up] and self.rect.y > 10:
            self.rect.y-= self.speed

        if keys_pressed[self.key_down] and self.rect.y < window_hight - 160:
            self.rect.y += self.speed

    def draw_player(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))



window_hight = 1000
window_weidth = 1300

main_win = display.set_mode((window_weidth, window_hight))
main_win.fill((175, 238, 238))

Player1 = Player(Color, 25, 150, 75, window_hight // 2 - 75, 5, K_Up = K_w, K_Down = K_s)
Player2 = Player(Color, 25, 150, 1200, window_hight // 2 - 75, 5, K_Up = K_UP, K_Down = K_DOWN)

clock = pygame.time.Clock()
piu_timer = 0

game = True
finish = False

while game:
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
           game = False

    if finish != True:
        main_win.fill((175, 238, 238))

        Player1.move_player()
        Player1.draw_player()

        Player2.move_player()
        Player2.draw_player()

    clock.tick(FPS)
    display.update()