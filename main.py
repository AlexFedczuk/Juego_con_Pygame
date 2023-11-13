import pygame

from constants import WIDTH, HEIGHT, FPS
from funtions import get_background, handle_move, draw, load_sprite_sheets, get_block
from classes import Player, Block, Fire, Proyectile
from assets.colores import BLACK

pygame.init()

pygame.display.set_caption("Juego en desarrollo...")

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
background, bg_image = get_background("Blue.png")    

offset_x = 0
scroll_area_width = 200

# Jugador
player = Player(100, 100, 50, 50, load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True))
# Objetos
block_size = 96
floor = [Block(i * block_size, HEIGHT - block_size, block_size, get_block) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]
fire = Fire(100, HEIGHT - block_size - 64, 16, 32, load_sprite_sheets)
fire.on()
objects = [
    *floor,
    Block(0, HEIGHT - block_size * 2, block_size, get_block),
    Block(block_size * 3, HEIGHT - block_size * 4, block_size, get_block),
    Block(block_size * 4, HEIGHT - block_size * 4, block_size, get_block),
    Block(block_size * 6, HEIGHT - block_size * 5, block_size, get_block),
    fire
]
bullets = []

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.jump_count < 2:
                player.jump()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            bullets.append(Proyectile(round(player.rect.x + player.rect.width // 2), round(player.rect.y + player.rect.height // 2), 6, BLACK, player.direction))
        player.loop(FPS)       
        fire.loop()
        Proyectile.loop(bullets)
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
            (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel    
pygame.quit()
quit()
# autopep8 --in-place --aggressive --aggressive main.py
# python -m tabnanny main.py