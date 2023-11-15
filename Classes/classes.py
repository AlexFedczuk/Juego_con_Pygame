from typing import Any
import pygame

from os import listdir
from os.path import isfile, join

from pygame.sprite import Group
from constants import COLOR, GRAVITY, ANIMATION_DELAY
#from funtions import load_sprite_sheets

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

class Fire(Object):
    def __init__(self, x, y, width, height, load_sprite_sheets) -> None:
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", 16, 32)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count // ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        # Update
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

    def blit(self, surface:pygame.Surface, offset_x):
        surface.blit(self.image, (self.rect.x - offset_x, self.rect.y))

    