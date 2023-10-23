from typing import Any
import pygame

from os import listdir
from os.path import isfile, join

from pygame.sprite import Group
from constants import COLOR, GRAVITY, ANIMATION_DELAY

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, load_sprite_sheets) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.SPRITES = load_sprite_sheets
        self.ANIMATION_DELAY = ANIMATION_DELAY
        self.jump_count = 0

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

    def jump(self):
        self.y_vel = -GRAVITY * 8 #Puede que esto no funcione...
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * GRAVITY) # Esto es para simular una gravedad/aceleracion "realista".
        self.move(self.x_vel, self.y_vel)
        self.fall_count += 1
        self.update_sprite() 

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1      

    def update_sprite(self) -> None:
        sprite_sheet = "idle"

        if self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect =  self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win:pygame.Surface, offset_x:int):
        # pygame.draw.rect(win, COLOR, self.rect)
        # self.sprite = self.SPRITES["idle_" + self.direction][0]        
        # self.sprite = pygame.image.load(r"05 - Pygame\Juego\assets\MainCharacters\MaskDude\fall.png")
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win:pygame.Surface, offset_x:int):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

class Block(Object):
    def __init__(self, x, y, size, get_block) -> None:
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def blit(self, surface:pygame.Surface, offset_x:int):
        surface.blit(self.image, (self.rect.x - offset_x, self.rect.y))