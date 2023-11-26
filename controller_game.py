import pygame

from constants import WIDTH, HEIGHT, FPS

from funtions import get_background, handle_move, draw, load_sprite_sheets, draw_rectangle, scroll_screen, create_map, controller_loop

from class_player import Player
from class_enemy import Enemy
from class_coin import Coin

def controller_play_game():
    pygame.display.set_caption("Juego en desarrollo... - Juego")

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")    

    offset_x = -200
    scroll_area_width = 200

    player = Player(0, 0, 50, 50, load_sprite_sheets("Player", "VirtualGuy", 32, 32, True), r"assets\Traps\Sand Mud Ice\Ice Particle.png")
    enemies = [
        Enemy(100, 0, 50, 50, load_sprite_sheets("Enemies", "NinjaFrog", 32, 32, True), r"assets\Traps\Sand Mud Ice\Mud Particle.png"),
        Enemy(250, 0, 50, 50, load_sprite_sheets("Enemies", "NinjaFrog", 32, 32, True), r"assets\Traps\Sand Mud Ice\Mud Particle.png")
    ]
    
    # Plataformas, suelo y trampas.
    objects = create_map()

    tecla_f1 = True
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
                if event.key == pygame.K_F1:
                    tecla_f1 = not tecla_f1
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and (len(player.proyectiles_shooted) < 3):
                player.proyectiles_shooted.append(player.create_proyectile(player.proyectile_image_path, player.direction))

        controller_loop(player, enemies, objects)      
        handle_move(player, objects, enemies, offset_x)
        draw(window, background, bg_image, player, objects, offset_x, enemies)

        offset_x = scroll_screen(player, offset_x, scroll_area_width)

        draw_rectangle(tecla_f1, window, player, objects, enemies, offset_x)
        pygame.display.update()