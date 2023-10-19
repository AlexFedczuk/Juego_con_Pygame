import pygame

from os import listdir
from os.path import isfile, join
from constants import COLOR, GRAVITY

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, load_sprite_sheets) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.SPRITES = load_sprite_sheets

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        # self.y_vel += min(1, (self.fall_count / fps) * GRAVITY) # Esto es para simular una gravedad/aceleracion "realista".
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def draw(self, win:pygame.Surface):
        # pygame.draw.rect(win, COLOR, self.rect)
        self.sprite = self.SPRITES["idle_" + self.direction][0]        
        #self.sprite = pygame.image.load(r"05 - Pygame\Juego\assets\MainCharacters\MaskDude\fall.png")
        win.blit(self.sprite, (self.rect.x, self.rect.y))