import pygame

from os import listdir
from os.path import isfile, join
from constants import WIDTH, HEIGHT, PLAYER_VEL
from classes import Player, Object

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

def draw(window:pygame.Surface, background, bg_image, player:Player, objects:list[pygame.Surface], offset_x:int):
    for tile in background:
        window.blit(bg_image, tile)

    for object in objects:
        object.blit(window, offset_x)

    player.draw(window, offset_x)

    pygame.display.update()

def collide(player:Player, objects:list[Object], dx:int) -> Object:
    player.move(dx, 0)
    player.update()

    collided_objects = None

    for object in objects:
        if pygame.sprite.collide_mask(player, object):
            collided_objects = object
            break

    player.move(-dx, 0)
    player.update

    return collided_objects


def handle_move(player:Player, objects:list[pygame.Surface]):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)
    """if keys[pygame.K_SPACE] and player.jump_count < 2:
        #if event.key == pygame.K_SPACE and player.jump_count < 2:
        player.jump()"""

    handle_vertical_collision(player, objects, player.y_vel)

def handle_vertical_collision(player:Player, objects:list[Object], dy:int) -> list[pygame.Surface]:
    collided_objects = []

    for object in objects:
        if pygame.sprite.collide_mask(player, object):
            if dy > 0:
                player.rect.bottom = object.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = object.rect.bottom
                player.hit_head()

        collided_objects.append(object)

    return collided_objects

        

# Esto da vuelta en el eje X los Sprites que le mandes.
def flip(sprites:list[pygame.sprite.Sprite]):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False) -> dict:
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

def get_block(size) -> pygame.Surface:
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)
