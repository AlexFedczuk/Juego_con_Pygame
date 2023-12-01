import pygame

from constants import WINDOW, BACK_GROUND_IMAGE, FONT_PATH, WIDTH
from colors import LIGHT_BROWN, SUPER_LIGHT_GREEN, WHITE

from funtions import get_font
from controller_option import controller_options_menu
from controller_niveles import controller_levels_menu

from class_button import Button_Text

def controller_main_menu():
    while True:
        pygame.display.set_caption("Juego en desarrollo... - Menu principal")

        WINDOW.blit(BACK_GROUND_IMAGE, (0, 0))

        mouse_position = pygame.mouse.get_pos()

        MAIN_MENU_TEXT = get_font(FONT_PATH, 50).render("MAIN MENU", True, LIGHT_BROWN)
        MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(WIDTH/2, 100))

        PALABRA = "PLAY"
        PLAY_BUTTON = Button_Text(pygame.image.load(r"assets\Play Rect.png"), WIDTH/2, 250, f"{PALABRA}", get_font(FONT_PATH, 25), SUPER_LIGHT_GREEN, WHITE)
        OPTIONS_BUTTON = Button_Text(pygame.image.load(r"assets\Options Rect.png"), WIDTH/2, 400, "OPTIONS", get_font(FONT_PATH, 25), SUPER_LIGHT_GREEN, WHITE)
        QUIT_BUTTON = Button_Text(pygame.image.load(r"assets\Quit Rect.png"), WIDTH/2, 550, "QUIT", get_font(FONT_PATH, 25), SUPER_LIGHT_GREEN, WHITE)

        WINDOW.blit(MAIN_MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.change_color(mouse_position)
            button.update(WINDOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Cerrando juego.")
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_BUTTON.check_input(mouse_position):
                    controller_levels_menu()
                if OPTIONS_BUTTON.check_input(mouse_position):
                    controller_options_menu()
                if QUIT_BUTTON.check_input(mouse_position):
                    print("Cerrando juego.")
                    pygame.quit()
                    quit()
        pygame.display.update()