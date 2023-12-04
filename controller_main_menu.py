import pygame

from constants import *
from colors import LIGHT_BROWN, SUPER_LIGHT_GREEN, WHITE

from funtions import get_font
from controller_option import controller_options_menu
from controller_niveles import controller_levels_menu

from class_button import Button_Text

def controller_main_menu():
    while True:
        pygame.display.set_caption(NAME_GAME + " - Menu principal")

        WINDOW.blit(BACK_GROUND_IMAGE, ORIGIN_POINT)

        mouse_position = pygame.mouse.get_pos()

        MAIN_MENU_TEXT = get_font(FONT_PATH, BIG_SIZE_FONT).render("MAIN MENU", True, LIGHT_BROWN)
        MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(WIDTH/2, 100))

        PALABRA = "PLAY"
        PLAY_BUTTON = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/3.2, f"{PALABRA}", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        OPTIONS_BUTTON = Button_Text(pygame.image.load(OPTIONS_RECT_PATH), WIDTH/2, HEIGHT/2, "OPTIONS", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        QUIT_BUTTON = Button_Text(pygame.image.load(QUIT_RECT_PATH), WIDTH/2, HEIGHT/1.45, "QUIT", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)

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