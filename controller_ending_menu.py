import pygame

from constants import *
from colors import *
from funtions import get_font, add_value_to_table

from class_button import Button_Text
from class_player import Player

def controller_ending_menu(player:Player, enemies_list:list, coins_list:list, remaining_seconds:int) -> bool:
    if len(enemies_list) == 0 and len(coins_list) == 0:
        window_title = NAME_GAME + " - You win!"
        menu_title = "YOU WIN!"
        return ending_menu(window_title, menu_title, player)
    elif player.live_status() or remaining_seconds <= 0:
        window_title = NAME_GAME + " - You lost..."
        menu_title = "YOU LOST..."
        return ending_menu(window_title, menu_title, player)
    return True

def ending_menu(window_title:str, menu_title:str, player:Player):
    while True:
        pygame.display.set_caption(window_title)
        WINDOW.blit(PAUSE_BACK_GROUND_IMAGE, (WIDTH/5, 0))

        mouse_position = pygame.mouse.get_pos()

        MAIN_MENU_TEXT = get_font(FONT_PATH, BIG_SIZE_FONT).render(menu_title, True, LIGHT_BROWN)
        MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(WIDTH/2, 100))

        PLAYER_SCORE = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/2, f"SCORE: {player.get_score()}", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        EXIT_BUTTON = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/1.2, "BACK TO MENU", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        WINDOW.blit(MAIN_MENU_TEXT, MENU_RECT)

        for buttons in [PLAYER_SCORE, EXIT_BUTTON]:
            buttons.change_color(mouse_position)
            buttons.update(WINDOW)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Cerrando juego.")
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if EXIT_BUTTON.check_input(mouse_position):
                    add_value_to_table(player.get_score(), "Coco", 'game_data_base.db')
                    return False
        pygame.display.update()