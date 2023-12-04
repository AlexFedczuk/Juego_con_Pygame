from funtions import load_constants_from_json

CONTANTS = load_constants_from_json(r'Configurations\constants.json')

"""constants = {
    "Player": {
        "PLAYER_VEL": 5,
        "PLAYER_HEALTH": 100,
        "GRAVITY": 1,
        "ANIMATION_DELAY": 4
    },
    "Enemy": {
        "ENEMY_HEALTH": 60,
        "ENEMY_VEL": 1
    },
    "Projectile": {
        "PROYECTILE_VELOCITY": 5,
        "RIGHT_EDGE_SCREEN": 1915,
        "LEFT_EDGE_SCREEN": -1055
    },
    "Screen": {
        "NAME_GAME": "Galactic Astronaut: Turtle Hunt",
        "ORIGIN_POINT": [0, 0],
        "WIDTH": 1000,
        "HEIGHT": 800,
        "FPS": 60,
        "CRITICAL_ALTITUDE": 736
    },
    "Rectangles": {
        "OPTIONS_RECT_PATH": r'assets\Rects\Options Rect.png',
        "PLAY_RECT_PATH": r'assets\Rects\Play Rect.png',
        "QUIT_RECT_PATH": r'assets\Rects\Quit Rect.png'
    },
    "Fonts": {
        "FONT_PATH": r"assets\Other\font.ttf",
        "BIG_SIZE_FONT": 50,
        "NORMAL_SIZE_FONT": 25,
        "SMALL_SIZE_FONT": 15
    },
    "Collision": {
        "COLLISION_TOLERANCE": 1
    },
    "Block": {
        "X_EARTH_PLATFORM": 96,
        "BLOCK_SIZE": 96,
        "BLOCK_X": 96,
        "BLOCK_Y": 800 - 96
    },
    "Projectiles": {
        "ICE_PARTICLE_IMG_PATH": r"assets\Traps\Sand Mud Ice\Ice Particle.png",
        "MUD_PARTICLE_IMG_PATH": r"assets\Traps\Sand Mud Ice\Mud Particle.png"
    },
    "Coins": {
        "COINS_VALUE": 10
    },
    "Buttons": {
        "CLOSE_BUTTON_IMG_PATH": r"assets\Menu\Buttons\Close.png"
    },
    "Timer": {
        "TIME": 10
    },
    "Other": {
        "BG_COLOR": [255, 255, 255],
        "COLOR": [255, 0, 0]
    }
}"""