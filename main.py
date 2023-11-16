import pygame

from constants import WIDTH, HEIGHT, FPS
from funtions import get_background, handle_move, draw, load_sprite_sheets, get_block, draw_rectangle, scroll_screen
from class_player import Player
from classe_block import Block
from class_fire import Fire

pygame.init()

pygame.display.set_caption("Juego en desarrollo...")

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
background, bg_image = get_background("Blue.png")    

offset_x = 0
scroll_area_width = 200

# Objetos
player = Player(0, 0, 50, 50, load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True), r"assets\Traps\Sand Mud Ice\Ice Particle.png")
# blocks = [Block(0, HEIGHT - block_size, block_size, get_block)]
block_size = 96
floor = [Block(i * block_size, HEIGHT - block_size, block_size, get_block) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]
fire = Fire(100, HEIGHT - block_size - 64, 16, 32, load_sprite_sheets)
fire.on()
objects = [
*floor,
    Block(0, HEIGHT - block_size * 2, block_size, get_block),
    Block(block_size * 6, HEIGHT - block_size * 2, block_size, get_block),
    Block(block_size * 3, HEIGHT - block_size * 4, block_size, get_block),
    Block(block_size * 4, HEIGHT - block_size * 4, block_size, get_block),
    Block(block_size * 6, HEIGHT - block_size * 5, block_size, get_block),
    fire
]
proyectile = None

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
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and (len(player.proyectiles_shooted) < 3):
            player.proyectiles_shooted.append(player.create_proyectile(player.proyectile_image_path))

    player.loop(FPS)
    fire.loop()
    handle_move(player, objects)
    draw(window, background, bg_image, player, objects, offset_x, proyectile)

    offset_x = scroll_screen(player, offset_x, scroll_area_width)

    draw_rectangle(window, player, objects, offset_x)
    pygame.display.update()
pygame.quit()