from classe_block import Block
from constants import *
from funtions import *

def create_map_level_1():
    objects = []

    background_assets = get_background("Blue.png")

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
        Fire(-355, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, True, FIRE_TURN_OFF_SOUND),
        Fire(355, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, True, FIRE_TURN_OFF_SOUND),
        Fire(1000, HEIGHT - BLOCK_SIZE - 64, 16, 32, load_sprite_sheets, True, FIRE_TURN_OFF_SOUND),
        Fire(845, 256, 16, 32, load_sprite_sheets, True, FIRE_TURN_OFF_SOUND),
        Fire(-125, 256, 16, 32, load_sprite_sheets, True, FIRE_TURN_OFF_SOUND)
    ]
    coins = [
        Coin(-275, 256, 16, 16, load_sprite_sheets, True, COIN_COLLECTED_SOUND),
        Coin(-465, 640, 16, 16, load_sprite_sheets, True, COIN_COLLECTED_SOUND),
        Coin(-175, 640, 16, 16, load_sprite_sheets, True, COIN_COLLECTED_SOUND),
        Coin(210, 640, 16, 16, load_sprite_sheets, True, COIN_COLLECTED_SOUND),
        Coin(1065, 640, 16, 16, load_sprite_sheets, True, COIN_COLLECTED_SOUND),
        Coin(970, 256, 16, 16, load_sprite_sheets, True, COIN_COLLECTED_SOUND),
        Coin(305, 160, 16, 16, load_sprite_sheets, True, COIN_COLLECTED_SOUND),
        Coin(355, 352, 16, 16, load_sprite_sheets, True, COIN_COLLECTED_SOUND)
    ]

    objects.extend(floor)
    objects.extend(floating_platforms)
    objects.extend(blocks)
    objects.extend(traps)
    objects.extend(coins)

    return [objects, background_assets]