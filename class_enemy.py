import pygame
from pygame import mixer

from constants import *
from class_proyectile import Proyectile
from class_health_bar import Health_Bar

class Enemy(pygame.sprite.Sprite):
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
        self.hit = False
        self.hit_count = 0
        self.proyectiles_shooted = []
        self.proyectile_image_path = proyectile_image_path
        self.vel = ENEMY_VEL
        self.health = ENEMY_HEALTH
        self.dead = False
        self.death_sound = DEATH_SOUND_PATH
        self.health_bar = Health_Bar(self.rect.x, self.rect.y, self.rect.width, HEALTH_BAR_HEIGHT, self.health)

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
        self.health -= 20

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
        self.health_bar.update_position(self.rect.x, self.rect.y)

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
        self.health_bar.draw(win, self.get_health(), offset_x)

    def create_proyectile(self, image_path:str, direction:str):
        return Proyectile(self.rect.x + 50, self.rect.y + 30, image_path, direction)
    
    def check_health(self):
        if self.health < 1:
            death_sound = mixer.Sound(self.death_sound)
            death_sound.play()
            self.dead = True
            return self.dead
        else:
            return False
        
    def get_health(self):
        return self.health