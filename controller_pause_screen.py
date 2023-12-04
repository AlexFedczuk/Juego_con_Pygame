import pygame

from constants import *
from colors import *
from funtions import get_font

from class_button import Button_Text

def controller_pause_menu():
    pygame.display.set_caption(NAME_GAME + " - Pause Menu")

    while True:
        WINDOW.blit(PAUSE_BACK_GROUND_IMAGE, (WIDTH/5, 0))

        mouse_position = pygame.mouse.get_pos()

        MAIN_MENU_TEXT = get_font(FONT_PATH, BIG_SIZE_FONT).render("PAUSE MENU", True, LIGHT_BROWN)
        MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(WIDTH/2, 100))

        CONTINUE_BUTTON = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/3.5, "CONTINUE", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        EXIT_BUTTON = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/1.2, "EXIT", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        WINDOW.blit(MAIN_MENU_TEXT, MENU_RECT)

        for button in [CONTINUE_BUTTON, EXIT_BUTTON]:
            button.change_color(mouse_position)
            button.update(WINDOW)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Cerrando juego.")
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if CONTINUE_BUTTON.check_input(mouse_position):
                    return True
                elif EXIT_BUTTON.check_input(mouse_position):
                    return False
        pygame.display.update()