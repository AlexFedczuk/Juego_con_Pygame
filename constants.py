import pygame
from pygame import mixer

mixer.init()

# Player
PLAYER_VEL = 5
PLAYER_HEALTH = 500
GRAVITY = 1
ANIMATION_DELAY = 4

# Enemy
ENEMY_HEALTH = 60
ENEMY_VEL = 1
ENEMY_VALUE = 10

# Velocidad del proyectile
PROYECTILE_VELOCITY = 5
# Izq. maximo deberia ser -1055. Der. maximo deberia ser 1855.
RIGHT_EDGE_SCREEN = 1915
LEFT_EDGE_SCREEN = -1055

# Pantalla
NAME_GAME = "Galactic Astronaut: Turtle Hunt"
ORIGIN_POINT = (0, 0)
WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
BACK_GROUND_IMAGE = pygame.transform.scale(pygame.image.load(r"assets\Background\Background.png"), (WIDTH, HEIGHT))
PAUSE_BACK_GROUND_IMAGE = pygame.transform.scale(BACK_GROUND_IMAGE, (WIDTH/1.6, HEIGHT))
CRITICAL_ALTITUDE = 736

# Rectangulos
OPTIONS_RECT_PATH = r'assets\Rects\Options Rect.png'
PLAY_RECT_PATH = r'assets\Rects\Play Rect.png'
QUIT_RECT_PATH = r'assets\Rects\Quit Rect.png'

# Fuentes
FONT_PATH = r"assets\Other\font.ttf"
BIG_SIZE_FONT = 50
NORMAL_SIZE_FONT = 25
SMALL_SIZE_FONT = 15

# Colision tolerante
COLLISION_TOLERANCE = 1

# Bloque
X_EARTH_PLATFORM = 96
BLOCK_SIZE = 96
BLOCK_X = BLOCK_SIZE
BLOCK_Y = HEIGHT - BLOCK_SIZE

# Proyectiles
ICE_PARTICLE_IMG_PATH = r"assets\Traps\Sand Mud Ice\Ice Particle.png"
MUD_PARTICLE_IMG_PATH = r"assets\Traps\Sand Mud Ice\Mud Particle.png"

# Coins
COINS_VALUE = 10

# Botones
CLOSE_BUTTON_IMG_PATH = r"assets\Menu\Buttons\Close.png"

# Temporizador
TIME = 5000

# Musica y Sonidos
MAIN_MENU_MUSIC = pygame.mixer.Sound(r'assets\Sounds\main_menu_music.ogg')
SHOOTING_SOUND = pygame.mixer.Sound(r'assets\Sounds\ball_shooted.wav')
FIRE_TURN_OFF_SOUND = pygame.mixer.Sound(r'assets\Sounds\fire_turn_off.wav')
PROYECTILE_COLLIDED_SOUND = pygame.mixer.Sound(r'assets\Sounds\proyectile_collided.wav')
COIN_COLLECTED_SOUND = pygame.mixer.Sound(r'assets\Sounds\coin_sound.wav')
DEATH_SOUND = pygame.mixer.Sound(r'assets\Sounds\enemy_death_sound.wav')
INITIAL_SOUND_VOLUMEN = 10

# Barra de Vida
HEALTH_BAR_HEIGHT = 10

# Otros
BG_COLOR = (255, 255, 255)
COLOR = (255, 0, 0)

