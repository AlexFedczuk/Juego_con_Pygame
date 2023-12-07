import pygame
import json
from typing import Callable

from os import listdir
from os.path import isfile, join
from constants import *
from colors import RED, BLUE, YELLOW, GREEN, PURPLE

from class_object import Object
from classe_block import Block
from class_fire import Fire
from class_player import Player
from class_proyectile import Proyectile
from class_enemy import Enemy
from class_coin import Coin
from class_button import Button

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

def draw(window:pygame.Surface, background, bg_image, player:Player, objects:list[pygame.Surface], offset_x:int, enemies:list[Enemy], exit_button:Button):
    for tile in background:
        window.blit(bg_image, tile)

    for object in objects:
        object.blit(window, offset_x)

    player.draw(window, offset_x)
    for enemy in enemies:
        enemy.draw(window, offset_x)

    draw_player_proyectiles(window, offset_x, player)
    exit_button.update(window)

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

def collide_proyectile(player:Player, enemies:list[Enemy], objects:list[Object]) -> Proyectile:
    collided_proyectile = None

    if player.proyectiles_shooted != []:
        for proyectile in player.proyectiles_shooted:
            if pygame.sprite.collide_mask(player, proyectile):
                collided_proyectile = proyectile
                break
            for object in objects:
                if not isinstance(object, Coin):
                    if isinstance(object, Fire) and object.animation_name == "off":
                        pass
                    else:
                        if pygame.sprite.collide_mask(object, proyectile):
                            player.proyectiles_shooted.remove(proyectile)
                            if isinstance(object, Fire):
                                object.off()
            for enemy in enemies:
                if pygame.sprite.collide_mask(enemy, proyectile):
                    player.proyectiles_shooted.remove(proyectile)
                    enemy.make_hit()
            if proyectile.rect.x > RIGHT_EDGE_SCREEN or proyectile.rect.x < LEFT_EDGE_SCREEN:
                    player.proyectiles_shooted.remove(proyectile)
                    break
    
    return collided_proyectile

def collect_coin(player:Player, objects:list[Object]) -> None:
    for object in objects:
        if isinstance(object, Coin):
            if object.rect.colliderect(player.rect):
                objects.remove(object)
                player.increase_score(COINS_VALUE)
                break

def collide_entities(player:Player, enemies:list[Enemy]):
    for enemy in enemies:
        if pygame.sprite.collide_mask(player, enemy):
            player.make_hit()
            break

def handle_movement(player:Player, objects:list[Object], enemies:list[Enemy], offset_x:int):
    handle_player_movement(player, objects)
    handle_enemies_movement(enemies, objects)
    collide_entities(player, enemies)
    collide_proyectile(player, enemies, objects)
    collect_coin(player, objects)

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
        if isinstance(object, Fire):
            if object.animation_name == "on":
                player.make_hit()

def handle_enemies_movement(enemies:list[Enemy], objects:list):
    for enemy in enemies:
        enemy.x_vel = 0

        enemy_collide_left = collide(enemy, objects, -ENEMY_VEL * 2)
        enemy_collide_right = collide(enemy, objects, ENEMY_VEL * 2)

        handle_vertical_collision(enemy, objects, enemy.y_vel)

        to_check = [enemy_collide_left, enemy_collide_right]

        for object in to_check:
            if isinstance(object, Block):
                if object.collidable == True:
                    enemy.vel = enemy.vel * -1

        if enemy.vel < 0:
            enemy.move_left(-enemy.vel)
        else:
            enemy.move_right(enemy.vel)        

def handle_vertical_collision(entity:Player or Enemy, objects:list[Object], dy:int) -> list[pygame.Surface]:
    collided_objects = []

    for object in objects:
        if not isinstance(object, Coin) and (not isinstance(object, Enemy) and not isinstance(object, Fire)):
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
    

def draw_rectangle(tecla:bool, window:pygame.Surface, player:Player, object_list:list[Object], enemies:list[Enemy], offset_x:int):
    if tecla:
        pygame.draw.rect(window, BLUE, (player.rect.x - offset_x, player.rect.y, player.rect.width, player.rect.height), 2) # 100, 200, 50, 100
        for object in object_list:
            pygame.draw.rect(window, GREEN, (object.rect.x - offset_x, object.rect.y, object.rect.width, object.rect.height), 2)
        for proyectile in player.proyectiles_shooted:
            pygame.draw.rect(window, RED, (proyectile.rect.x - offset_x, proyectile.rect.y, proyectile.rect.width, proyectile.rect.height), 2)
        if len(enemies) > 0:
            for enemy in enemies:
                pygame.draw.rect(window, YELLOW, (enemy.rect.x - offset_x, enemy.rect.y, enemy.rect.width, enemy.rect.height), 2)

            for object in object_list:
                if object.rect.colliderect(enemies[0]):
                    pygame.draw.rect(window, PURPLE, (object.rect.x - offset_x, object.rect.y, object.rect.width, object.rect.height), 2)

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
        Block(BLOCK_SIZE * -6, HEIGHT - BLOCK_SIZE * 0, get_block, BLOCK_SIZE, X_EARTH_PLATFORM, "floor", False),
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
        Fire(-355, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, True),
        Fire(355, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, True),
        Fire(1000, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, True),
        Fire(845, 256, 16, 32, load_sprite_sheets, True),
        Fire(-125, 256, 16, 32, load_sprite_sheets, True)
    ]
    coins = [
        Coin(-275, 256, 16, 16, load_sprite_sheets, True),
        Coin(-465, 640, 16, 16, load_sprite_sheets, True),
        Coin(-175, 640, 16, 16, load_sprite_sheets, True),
        Coin(210, 640, 16, 16, load_sprite_sheets, True),
        Coin(1065, 640, 16, 16, load_sprite_sheets, True),
        Coin(970, 256, 16, 16, load_sprite_sheets, True),
        Coin(305, 160, 16, 16, load_sprite_sheets, True),
        Coin(355, 352, 16, 16, load_sprite_sheets, True)
    ]

    objects.extend(floor)
    objects.extend(floating_platforms)
    objects.extend(blocks)
    objects.extend(traps)
    objects.extend(coins)

    return objects

def controller_loop(player:Player, enemies:list[Enemy], objects:list):
    if player != None:
        player.loop(FPS)

    if len(enemies) > 0:
        for enemy in enemies:
            enemy.loop(FPS)
            if enemy.check_health():
                enemies.remove(enemy)
                player.increase_score(ENEMY_VALUE)

    for object in objects:
        if isinstance(object, Fire):
            object.loop()
        elif isinstance(object, Coin):
            object.loop()

def pause_game():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                elif event.key  == pygame.K_q:
                    return False
        print("Press 'c' to continue or press 'q' to quit.")    
    return True

def check_events(runing:bool, f1_key:bool, events_list:list[pygame.event.Event], mouse_position:tuple, player:Player, controller_pause_menu:Callable, exit_button:Button) -> tuple:
    result_runing = runing
    result_f1_key = f1_key

    for event in events_list:
            if event.type == pygame.QUIT:
                print("Cerrando juego.")
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
                elif event.key == pygame.K_ESCAPE:
                    result_runing = controller_pause_menu()
                elif event.key == pygame.K_F1:
                    result_f1_key = not result_f1_key
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if len(player.proyectiles_shooted) < 3:
                    player.proyectiles_shooted.append(player.create_proyectile(player.proyectile_image_path, player.direction, SHOOTING_SOUND))
                if exit_button.check_input(mouse_position):
                    result_runing = False            
    return (result_runing, result_f1_key)

def format_time(total_seconds:int, elapsed_seconds:int):
    remaining_seconds = total_seconds - elapsed_seconds
    #print(f"remaining_seconds: {remaining_seconds}")

    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    remaining_seconds = remaining_seconds % 60

    return f"{hours}:{minutes}:{remaining_seconds}"

def load_constants_from_json(file_path:str):
    try:
        with open(file_path, 'r') as file:
            constants = json.load(file)
        return constants
    except FileNotFoundError:
        print(f'Error: El archivo {file_path} no se encontró.')
        return None
    except json.JSONDecodeError:
        print(f'Error: No se pudo decodificar el archivo {file_path} como JSON.')
        return None
    
def map_value(value, from_low, from_high, to_low, to_high):
    value = max(min(value, from_high), from_low)
    proportion = (value - from_low) / (from_high - from_low)
    mapped_value = to_low + proportion * (to_high - to_low)

    return mapped_value
