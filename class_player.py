import pygame

from constants import *
from class_proyectile import Proyectile

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, load_sprite_sheets, proyectile_image_path:str) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.SPRITES = load_sprite_sheets
        self.ANIMATION_DELAY = ANIMATION_DELAY
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.proyectiles_shooted = []
        self.proyectile_image_path = proyectile_image_path
        self.health = PLAYER_HEALTH
        self.dead = False
        self.score = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def jump(self):
        self.y_vel = -GRAVITY * 8 #Puede que esto no funcione...
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def make_hit(self):
        self.hit = True
        self.hit_count = 0
        self.health -= 10

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * GRAVITY) # Esto es para simular una gravedad/aceleracion "realista".
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()
        self.check_health()
        self.check_altitude()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1      

    def update_sprite(self) -> None:
        sprite_sheet = "idle"

        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect =  self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win:pygame.Surface, offset_x:int):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

    def create_proyectile(self, image_path:str, direction:str):
        return Proyectile(self.rect.x + 50, self.rect.y + 30, image_path, direction)
    
    def check_health(self):
        if self.health < 1:
            self.die()

    def increase_score(self, points:int):
        self.score += points

    def check_altitude(self):
        if self.rect.y >= CRITICAL_ALTITUDE:
            self.die()
    
    def die(self):
        self.dead = True

    def live_status(self) -> bool:
        return self.dead
    
    def get_score(self) -> int:
        return self.score