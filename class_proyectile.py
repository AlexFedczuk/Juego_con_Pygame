import pygame

from constants import PROYECTILE_VELOCITY

class Proyectile(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, image_path:str, direction:str) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)# assets\Traps\Sand Mud Ice\Ice Particle.png
        self.rect = self.image.get_rect(center = (x, y))
        self.direction = direction
    
    def update(self) -> None:
        if self.direction == "left":
            self.rect.x += -PROYECTILE_VELOCITY
        elif self.direction == "right":
            self.rect.x += PROYECTILE_VELOCITY

    def delete(self):
        del self