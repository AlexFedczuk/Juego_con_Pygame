import pygame

from constants import WINDOW, FPS
from funtions import *

from class_player import Player
from class_enemy import Enemy
from class_button import Button
from controller_pause_screen import controller_pause_menu
from controller_ending_menu import controller_ending_menu

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
    objects = create_map()

    tecla_f1 = True
    runing = True
    while runing:
        clock.tick(FPS)
        runing, tecla_f1 = check_events(pygame.event.get(), pygame.mouse.get_pos(), player, controller_pause_menu, EXIT_BUTTON, tecla_f1)
            
        controller_loop(player, enemies, objects, )
        handle_movement(player, objects, enemies, offset_x)
        draw(WINDOW, background, bg_image, player, objects, offset_x, enemies, EXIT_BUTTON)

        offset_x = scroll_screen(player, offset_x, scroll_area_width)

        draw_rectangle(tecla_f1, WINDOW, player, objects, enemies, offset_x)

        coins = []
        for object in objects:
            if isinstance(object, Coin):
                coins.append(object)
        runing = controller_ending_menu(player.live_status(), enemies, coins)
        #print(f"X: {player.rect.x} - Y: {player.rect.y} - Is he dead? {player.dead}")
        pygame.display.update()