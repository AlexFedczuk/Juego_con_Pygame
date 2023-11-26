import pygame

from typing import Callable
from class_object import Object
from constants import ANIMATION_DELAY

class Coin(Object): # assets\Items\Coins\coin_rot_anim.png
    def __init__(self, x:int, y:int, width:int, height:int, load_sprite_sheets:Callable, collectible:bool) -> None:
        super().__init__(x, y, width, height, "fire")
        self.coin = load_sprite_sheets("Items", "Coins", 32, 32)
        self.image = self.coin["coin_rot_anim"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "coin_rot_anim"
        self.collectible = collectible

    def loop(self):
        sprites = self.coin[self.animation_name]
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