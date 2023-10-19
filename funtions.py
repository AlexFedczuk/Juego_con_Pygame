import pygame

from os import listdir
from os.path import isfile, join
from constants import WIDTH, HEIGHT, PLAYER_VEL
from classes import Player

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    print(f"image {image}")
    # image = pygame.image.load(r"05 - Pygame\Juego\assets\Background\Blue.png")
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)

    return tiles, image

def draw(window:pygame.Surface, background, bg_image, player:Player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update()

def handle_move(player:Player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

# Esto da vuelta en el eje X los Sprites que le mandes.
def flip(sprites:list[pygame.sprite.Sprite]):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
        path = join("assets", dir1, dir2)
        images = [f for f in listdir(path) if isfile(join(path, f))]

        all_sprites = {}

        for image in images:
            sprite_sheets = pygame.image.load(join(path, image)).convert_alpha()

            sprites = []
            for i in range(sprite_sheets.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheets, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            else:
                all_sprites[image.replace(".png", "")] = sprites

        return all_sprites