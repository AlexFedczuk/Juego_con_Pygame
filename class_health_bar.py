import pygame

class Health_Bar():
    def __init__(self, x:int, y:int, width:int, height:int, max_health:int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = max_health
        self.max_health = max_health

    def draw(self, window:pygame.Surface, actual_health:int, offset_x:int):
        self.health = self.update_health_bar(actual_health)
        ratio = self.health / self.max_health
        pygame.draw.rect(window, "red", (self.x - offset_x, self.y, self.width, self.height))
        pygame.draw.rect(window, "green", (self.x - offset_x, self.y, self.width * ratio, self.height))

    def update_health_bar(self, actual_health:int):
        return actual_health

    def update_position(self, x:int, y: int):
        self.x = x
        self.y = y