from typing import Any
import pygame
from pygame.sprite import _Group

class Proyectile(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (x, y))
    
    def update(self) -> None:
        self.rect.x += 5