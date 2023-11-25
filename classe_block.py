import pygame

from typing import Callable
from class_object import Object

class Block(Object):
    def __init__(self, x:int, y:int, get_block:Callable, size:int, x_platform_img:int, name:str) -> None:
        super().__init__(x, y, size, size)
        block = get_block(size, x_platform_img)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.name = name

    def blit(self, surface:pygame.Surface, offset_x:int):
        surface.blit(self.image, (self.rect.x - offset_x, self.rect.y))