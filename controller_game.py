import pygame

from constants import WIDTH, HEIGHT, FPS, BLOCK_SIZE, BLOCK_X, BLOCK_Y
from funtions import get_background, handle_move, draw, load_sprite_sheets, get_block, draw_rectangle, scroll_screen
from class_player import Player
from classe_block import Block
from class_fire import Fire
from class_enemy import Enemy

def controller_play_game():
    pygame.display.set_caption("Juego en desarrollo... - Juego")

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")    

    offset_x = 0
    scroll_area_width = 200

    # Objetos
    player = Player(0, 0, 50, 50, load_sprite_sheets("Player", "VirtualGuy", 32, 32, True), r"assets\Traps\Sand Mud Ice\Ice Particle.png")
    enemies = [
        Enemy(100, 0, 50, 50, load_sprite_sheets("Enemies", "NinjaFrog", 32, 32, True), r"assets\Traps\Sand Mud Ice\Mud Particle.png"),
        Enemy(250, 0, 50, 50, load_sprite_sheets("Enemies", "NinjaFrog", 32, 32, True), r"assets\Traps\Sand Mud Ice\Mud Particle.png")
    ]
    floor = [
        Block(i * BLOCK_SIZE, BLOCK_Y, BLOCK_SIZE, get_block, "floor") for i in range(-WIDTH // BLOCK_SIZE, WIDTH * 2 // BLOCK_SIZE)
    ]
    blocks = [
        Block(BLOCK_SIZE * 0, BLOCK_Y * 2, BLOCK_SIZE, get_block, "block"),
        Block(BLOCK_SIZE * 6, BLOCK_Y * 2, BLOCK_SIZE, get_block, "block"),
        Block(BLOCK_SIZE * 3, BLOCK_Y * 4, BLOCK_SIZE, get_block, "block"),
        Block(BLOCK_SIZE * 4, BLOCK_Y * 4, BLOCK_SIZE, get_block, "block"),
        Block(BLOCK_SIZE * 6, BLOCK_Y * 6, BLOCK_SIZE, get_block, "block"),
        Block(BLOCK_SIZE * 7, BLOCK_Y * 5, BLOCK_SIZE, get_block, "block"),
    ]
    traps = [
        Fire(100, BLOCK_Y - 64, 16, 32, load_sprite_sheets)
    ]
    
    # Plataformas, suelo y trampas.
    objects = []
    objects.extend(floor)
    objects.extend(blocks)
    objects.extend(traps)

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
                player.proyectiles_shooted.append(player.create_proyectile(player.proyectile_image_path, player.direction))

        player.loop(FPS)
        for enemy in enemies:
            enemy.loop(FPS)
        for trap in traps:
            trap.loop()        
        handle_move(player, objects, enemies, offset_x)
        draw(window, background, bg_image, player, objects, offset_x, enemies)

        offset_x = scroll_screen(player, offset_x, scroll_area_width)

        draw_rectangle(window, player, objects, enemies, offset_x)
        #print(f"Posicion x del jugador: {player.rect.x}") # Izq. maximo deberia ser -1055. Der. maximo deberia ser 1855.
        pygame.display.update()