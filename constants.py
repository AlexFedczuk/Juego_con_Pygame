import pygame

BG_COLOR = (255, 255, 255)
COLOR = (255, 0, 0)
FPS = 60
PLAYER_VEL = 5
ENEMY_VEL = 1
GRAVITY = 1
ANIMATION_DELAY = 4
# Velocidad del proyectile
PROYECTILE_VELOCITY = 5
# Izq. maximo deberia ser -1055. Der. maximo deberia ser 1855.
RIGHT_EDGE_SCREEN = 1915
LEFT_EDGE_SCREEN = -1055
# Pantalla
WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BACK_GROUND_IMAGE = pygame.transform.scale(pygame.image.load(r"assets\Background.png"), (WIDTH, HEIGHT))
# Fuentes
FONT_PATH = r"assets\font.ttf"
# Colision tolerante
COLLISION_TOLERANCE = 1