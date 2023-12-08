import pygame
from pygame import mixer
from typing import Callable

from class_object import Object
from constants import *

class Fire(Object):
    def __init__(self, x:int, y:int, width:int, height:int, load_sprite_sheets:Callable, collidable:bool, fire_turn_off_sound:pygame.mixer.Sound) -> None:
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", 16, 32)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "on"
        self.collidable = collidable
        self.fire_turn_off_sound = fire_turn_off_sound
        

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.fire_turn_off_sound.play()
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