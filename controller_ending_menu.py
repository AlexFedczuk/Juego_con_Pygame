import pygame

from constants import WINDOW, FONT_PATH, WIDTH, PAUSE_BACK_GROUND_IMAGE
from colors import WHITE, LIGHT_BROWN, SUPER_LIGHT_GREEN
from funtions import get_font

from class_button import Button_Text

def controller_ending_menu(player_status:bool, enemies_list:list, coins_list:list) -> bool:
    # print(f"player is dead? {player_status} - lista de enemigos: {len(enemies_list)} - lista de monedas: {len(coins_list)}")
    if len(enemies_list) == 0 and len(coins_list) == 0:
        runing = True
        window_title = "Juego en desarrollo... - You win!"
        menu_title = "YOU WIN!"
    elif player_status:
        runing = True
        window_title = "Juego en desarrollo... - You lost..."
        menu_title = "YOU LOST..."
    else:
        runing = False

    while runing:
        pygame.display.set_caption(window_title)
        WINDOW.blit(PAUSE_BACK_GROUND_IMAGE, (200, 0))

        mouse_position = pygame.mouse.get_pos()

        MAIN_MENU_TEXT = get_font(FONT_PATH, 50).render(menu_title, True, LIGHT_BROWN)
        MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(WIDTH/2, 100))

        EXIT_BUTTON = Button_Text(pygame.image.load(r"assets\Play Rect.png"), WIDTH/2, 650, "BACK TO MENU", get_font(FONT_PATH, 25), SUPER_LIGHT_GREEN, WHITE)
        WINDOW.blit(MAIN_MENU_TEXT, MENU_RECT)

        EXIT_BUTTON.change_color(mouse_position)
        EXIT_BUTTON.update(WINDOW)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Cerrando juego.")
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if EXIT_BUTTON.check_input(mouse_position):
                    return False
        pygame.display.update()
    return True