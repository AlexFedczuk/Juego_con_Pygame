import pygame

from class_object import Object

class Block(Object):
    def __init__(self, x, y, size, get_block) -> None:
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def blit(self, surface:pygame.Surface, offset_x:int):
        surface.blit(self.image, (self.rect.x - offset_x, self.rect.y))