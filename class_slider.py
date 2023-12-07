import pygame

class Slider():
    def __init__(self, x:int, y:int, width:int, height:int, initial_value:float, min:int, max:int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.slider_left_position = self.x - (self.width // 2)
        self.slider_right_position = self.x + (self.width // 2)
        self.slider_top_position = self.y - (self.height // 2)

        self.min = min
        self.max = max
        self.initial_value = (self.slider_right_position - self.slider_left_position) * initial_value

        self.container_rect = pygame.Rect(self.slider_left_position, self.slider_top_position, self.width, self.height)
        self.button_rect = pygame.Rect(self.slider_left_position + self.initial_value - 5, self.slider_top_position, 20, self.height)

    def render(self, window:pygame.Surface):
        pygame.draw.rect(window, "darkgray", self.container_rect)
        pygame.draw.rect(window, "blue", self.button_rect)

    def move_slider(self, mouse_position):
        self.button_rect.centerx = mouse_position[0]

        """if self.button_rect.x < self.container_rect.x:
            self.button_rect.x += 1
        if self.button_rect.x > self.container_rect.width:
            self.button_rect.x -= 1""" 
    def get_value(self):
        value_range = self.slider_right_position - self.slider_left_position
        button_value = self.button_rect.centerx - self.slider_left_position

        return (button_value/value_range) * (self.max - self.min) + self.min

