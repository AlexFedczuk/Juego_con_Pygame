import pygame

from constants import WINDOW, FPS
from funtions import get_background, handle_move, draw, load_sprite_sheets, draw_rectangle, scroll_screen, create_map, controller_loop, pause_game

from class_player import Player
from class_enemy import Enemy
from class_button import Button
from controller_pause_screen import controller_pause_menu
# assets\Menu\Buttons\Close.png

def controller_play_game():
    pygame.display.set_caption("Juego en desarrollo... - Juego")

    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")    

    offset_x = -200
    scroll_area_width = 200

    player = Player(0, 0, 50, 50, load_sprite_sheets("Player", "VirtualGuy", 32, 32, True), r"assets\Traps\Sand Mud Ice\Ice Particle.png")
    enemies = [
        Enemy(100, 0, 50, 50, load_sprite_sheets("Enemies", "NinjaFrog", 32, 32, True), r"assets\Traps\Sand Mud Ice\Mud Particle.png"),
        Enemy(250, 0, 50, 50, load_sprite_sheets("Enemies", "NinjaFrog", 32, 32, True), r"assets\Traps\Sand Mud Ice\Mud Particle.png")
    ]
    
    EXIT_BUTTON = Button(pygame.image.load(r"assets\Menu\Buttons\Close.png"), 10, 10)
    # Plataformas, suelo y trampas.
    objects = create_map()

    tecla_f1 = True
    runing = True
    while runing:
        clock.tick(FPS)
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Cerrando juego.")
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
                elif event.key == pygame.K_F1:
                    tecla_f1 = not tecla_f1
                elif event.key == pygame.K_ESCAPE:
                    runing = controller_pause_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if len(player.proyectiles_shooted) < 3:
                    player.proyectiles_shooted.append(player.create_proyectile(player.proyectile_image_path, player.direction))
                if EXIT_BUTTON.checkForInput(mouse_position):
                    runing = False
            

        controller_loop(player, enemies, objects)
        handle_move(player, objects, enemies, offset_x)
        draw(WINDOW, background, bg_image, player, objects, offset_x, enemies, EXIT_BUTTON)

        offset_x = scroll_screen(player, offset_x, scroll_area_width)

        draw_rectangle(tecla_f1, WINDOW, player, objects, enemies, offset_x)
        #print(f"X: {player.rect.x} - Y: {player.rect.y}")
        pygame.display.update()