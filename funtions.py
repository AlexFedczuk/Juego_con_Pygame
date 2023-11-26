import pygame

from os import listdir
from os.path import isfile, join
from constants import WIDTH, HEIGHT, PLAYER_VEL, RIGHT_EDGE_SCREEN, LEFT_EDGE_SCREEN, ENEMY_VEL, WINDOW, BLOCK_SIZE, X_EARTH_PLATFORM, FPS
from colors import RED, BLUE, YELLOW, GREEN, PURPLE

from class_object import Object
from classe_block import Block
from class_fire import Fire
from class_player import Player
from class_proyectile import Proyectile
from class_enemy import Enemy

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    # image = pygame.image.load(r"05 - Pygame\Juego\assets\Background\Blue.png")
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)

    return tiles, image

def draw(window:pygame.Surface, background, bg_image, player:Player, objects:list[pygame.Surface], offset_x:int, enemies:list[Enemy]):
    for tile in background:
        window.blit(bg_image, tile)

    for object in objects:
        object.blit(window, offset_x)

    player.draw(window, offset_x)
    for enemy in enemies:
        enemy.draw(window, offset_x)

    draw_player_proyectiles(window, offset_x, player)

def collide(entity:Player or Enemy, objects:list[Object], dx:int) -> Object:
    entity.move(dx, 0)
    entity.update()

    collided_objects = None

    for object in objects:
        if pygame.sprite.collide_mask(entity, object):
            collided_objects = object
            break

    entity.move(-dx, 0)
    entity.update

    return collided_objects

def collide_proyectile(player:Player, objects:list[Object]) -> Proyectile:
    collided_proyectile = None

    if player.proyectiles_shooted != []:
        for proyectile in player.proyectiles_shooted:
            if pygame.sprite.collide_mask(player, proyectile):
                collided_proyectile = proyectile
                break
            for object in objects:
                if pygame.sprite.collide_mask(object, proyectile):
                    player.proyectiles_shooted.remove(proyectile)
                    break
            if proyectile.rect.x > RIGHT_EDGE_SCREEN or proyectile.rect.x < LEFT_EDGE_SCREEN:
                    player.proyectiles_shooted.remove(proyectile)
                    break
    
    return collided_proyectile

def handle_move(player:Player, objects:list[Object], enemies:list[Enemy], offset_x:int):
    handle_player_movement(player, objects)
    handle_enemies_movement(enemies, objects)
    collide_proyectile(player, objects)

def handle_player_movement(player:Player, objects:list[Object]):
    keys = pygame.key.get_pressed()

    player.x_vel = 0

    player_collide_left = collide(player, objects, -PLAYER_VEL * 2)
    player_collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_a] and not player_collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_d] and not player_collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)

    to_check = [player_collide_left, player_collide_right, *vertical_collide]

    for object in to_check:
        if object and (object.name == "fire" and object.collidable == True):
            player.make_hit()

def handle_enemies_movement(enemies:list[Enemy], objects:list[Object]):
    for enemy in enemies:
        enemy.x_vel = 0

        enemy_collide_left = collide(enemy, objects, -ENEMY_VEL * 2)
        enemy_collide_right = collide(enemy, objects, ENEMY_VEL * 2)

        handle_vertical_collision(enemy, objects, enemy.y_vel)

        to_check = [enemy_collide_left, enemy_collide_right]

        for object in to_check:
            if object and object.collidable == True:
                enemy.vel = enemy.vel * -1

        if enemy.vel < 0:
            enemy.move_left(-enemy.vel)
        else:
            enemy.move_right(enemy.vel)        

def handle_vertical_collision(entity:Player or Enemy, objects:list[Object], dy:int) -> list[pygame.Surface]:
    collided_objects = []

    for object in objects:
        if pygame.sprite.collide_mask(entity, object):
            if dy > 0:
                entity.rect.bottom = object.rect.top
                entity.landed()
            elif dy < 0:
                entity.rect.top = object.rect.bottom
                entity.hit_head()

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

def get_block(size:int, x_terrain_img:int) -> pygame.Surface:
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(x_terrain_img, 0, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def scroll_screen(player:Player, offset_x:int, scroll_area_width:int) -> int:
    if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
        (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
        offset_x += player.x_vel
    return offset_x
    

def draw_rectangle(tecla_f1:bool, window:pygame.Surface, player:Player, object_list:list[Object], enemies:list[Enemy], offset_x:int):
    if tecla_f1:
        pygame.draw.rect(window, BLUE, (player.rect.x - offset_x, player.rect.y, player.rect.width, player.rect.height), 2) # 100, 200, 50, 100
        for object in object_list:
            pygame.draw.rect(window, GREEN, (object.rect.x - offset_x, object.rect.y, object.rect.width, object.rect.height), 2)
        for proyectile in player.proyectiles_shooted:
            pygame.draw.rect(window, RED, (proyectile.rect.x - offset_x, proyectile.rect.y, proyectile.rect.width, proyectile.rect.height), 2)
        for enemy in enemies:
            pygame.draw.rect(window, YELLOW, (enemy.rect.x - offset_x, enemy.rect.y, enemy.rect.width, enemy.rect.height), 2)

        for object in object_list:
            if object.rect.colliderect(enemies[0]):
                pygame.draw.rect(WINDOW, PURPLE, (object.rect.x - offset_x, object.rect.y, object.rect.width, object.rect.height), 2)

def draw_player_proyectiles(window:pygame.Surface, offset_x:int, player:Player):
    if player.proyectiles_shooted != []:
        for proyectile in player.proyectiles_shooted:
                window.blit(proyectile.image, (proyectile.rect.x - offset_x, proyectile.rect.y))
                proyectile.update()

def get_font(font:str, size:int) -> pygame.font.Font: # Returns Press-Start-2P in the desired size
    return pygame.font.Font(font, size)

def create_map():
    objects = []

    floor = [
        Block(BLOCK_SIZE * -5, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * -4, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * -3, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * -2, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * -1, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 0, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 1, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 2, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 3, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 4, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 5, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 6, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 7, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 8, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 9, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 10, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
        Block(BLOCK_SIZE * 11, HEIGHT - BLOCK_SIZE * 1, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False)    
    ]
    floating_platforms = [
        # Plataforma del medio-arriba.
        Block(BLOCK_SIZE * 2, HEIGHT - BLOCK_SIZE * 6, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * 3, HEIGHT - BLOCK_SIZE * 6, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * 4, HEIGHT - BLOCK_SIZE * 6, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        # Plataforma del medio-abajo.
        Block(BLOCK_SIZE * 3, HEIGHT - BLOCK_SIZE * 4, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * 4, HEIGHT - BLOCK_SIZE * 4, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        # Plataforma de la derecha.
        Block(BLOCK_SIZE * 7, HEIGHT - BLOCK_SIZE * 5, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * 8, HEIGHT - BLOCK_SIZE * 5, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * 9, HEIGHT - BLOCK_SIZE * 5, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * 10, HEIGHT - BLOCK_SIZE * 5, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        # Plataforma de la izquierda.
        Block(BLOCK_SIZE * 0, HEIGHT - BLOCK_SIZE * 5, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * -1, HEIGHT - BLOCK_SIZE * 5, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * -2, HEIGHT - BLOCK_SIZE * 5, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
        Block(BLOCK_SIZE * -3, HEIGHT - BLOCK_SIZE * 5, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floating_platform", True),
    ]   
    blocks = [
        # Obstaculo de la izquierda.
        Block(BLOCK_SIZE * 0, HEIGHT - BLOCK_SIZE * 2, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "obstacle", True),
        # Obstaculo de la derecha.
        Block(BLOCK_SIZE * 6, HEIGHT - BLOCK_SIZE * 2, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "obstacle", True),
    ]
    traps = [
        Fire(-355, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, False),
        Fire(355, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, False),
        Fire(1000, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, False),
        Fire(845, 256, 16, 32, load_sprite_sheets, False),
        Fire(-125, 256, 16, 32, load_sprite_sheets, False)
    ]

    objects.extend(floor)
    objects.extend(floating_platforms)
    objects.extend(blocks)
    objects.extend(traps)

    return objects

def controller_loop(player:Player, enemies:list[Enemy], objects:list):
    player.loop(FPS)

    for enemy in enemies:
        enemy.loop(FPS)

    for object in objects:
        if isinstance(object, Fire):
            object.loop()

