import pygame

from constants import WIDTH

class Proyectile(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path:str) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)# assets\Traps\Sand Mud Ice\Ice Particle.png
        self.rect = self.image.get_rect(center = (x, y))        
    
    def update(self) -> None:
        self.rect.x += 5

    def delete(self):
        del self