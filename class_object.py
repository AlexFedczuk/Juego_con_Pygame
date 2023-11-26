import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, width:int, height:int, name=None, collidable=None) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        self.collidable = collidable

    def draw(self, win:pygame.Surface, offset_x:int):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))