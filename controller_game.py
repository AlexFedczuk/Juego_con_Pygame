import pygame

from constants import *
from funtions import *

from class_player import Player
from class_enemy import Enemy
from class_button import Button, Button_Dynamic_Text
from controller_pause_screen import controller_pause_menu
from controller_ending_menu import controller_ending_menu
from colors import BLACK

def controller_play_game():
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")    

    offset_x = -200
    scroll_area_width = 200

    player = Player(0, 0, 50, 50, load_sprite_sheets("Player", "VirtualGuy", 32, 32, True), ICE_PARTICLE_IMG_PATH)
    enemies = [
        Enemy(100, 0, 50, 50, load_sprite_sheets("Enemies", "NinjaFrog", 32, 32, True), MUD_PARTICLE_IMG_PATH),
        Enemy(250, 0, 50, 50, load_sprite_sheets("Enemies", "NinjaFrog", 32, 32, True), MUD_PARTICLE_IMG_PATH)
    ]
    objects = create_map()
    EXIT_BUTTON = Button(pygame.image.load(CLOSE_BUTTON_IMG_PATH), 10, 10)

    # Timer
    start_time = pygame.time.get_ticks()
    time = TIME
    TIMER = Button_Dynamic_Text(pygame.transform.scale(pygame.image.load(PLAY_RECT_PATH), (321, 90)), 180, 100, "", get_font(FONT_PATH, SMALL_SIZE_FONT), BLACK, BLACK)

    f1_key = False
    runing = True
    while runing:
        pygame.display.set_caption(NAME_GAME + " - Level 1")
        
        clock.tick(FPS)
        elapsed_time = pygame.time.get_ticks() - start_time
        events_list = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()

        coins = [obj for obj in objects if isinstance(obj, Coin)]
        runing = controller_ending_menu(player.live_status(), enemies, coins, (time - (elapsed_time // 1000)))

        result = check_events(runing, f1_key, events_list, mouse_position, player, controller_pause_menu, EXIT_BUTTON)
        runing = result[0]
        f1_key = result[1]

        controller_loop(player, enemies, objects, TIMER)
        handle_movement(player, objects, enemies, offset_x)        
        draw(WINDOW, background, bg_image, player, objects, offset_x, enemies, EXIT_BUTTON)
        TIMER.update(WINDOW, "Time remaning " + format_time(time, (elapsed_time // 1000)))

        offset_x = scroll_screen(player, offset_x, scroll_area_width)

        draw_rectangle(f1_key, WINDOW, player, objects, enemies, offset_x)
        pygame.display.update()