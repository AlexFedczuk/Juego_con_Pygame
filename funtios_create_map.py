from level_one_map import create_map_level_1
from level_two_map import create_map_level_2
from level_three_map import create_map_level_3

def create_map(level:bool):
    if level == 1:
        maps_assets = create_map_level_1()
        objects = maps_assets[0]
        background_assets = maps_assets[1]
        background = background_assets[0]
        bg_image = background_assets[1]
        enemies = maps_assets[2]
    elif level == 2:
        maps_assets = create_map_level_2()
        objects = maps_assets[0]
        background_assets = maps_assets[1]
        background = background_assets[0]
        bg_image = background_assets[1]
        enemies = maps_assets[2]
    elif level == 3:
        maps_assets = create_map_level_3()
        objects = maps_assets[0]
        background_assets = maps_assets[1]
        background = background_assets[0]
        bg_image = background_assets[1]
        enemies = maps_assets[2]
    else:
        return None
    
    return [objects, background, bg_image, enemies]