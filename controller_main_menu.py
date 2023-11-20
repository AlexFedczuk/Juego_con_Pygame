import pygame, sys

from constants import WINDOW, BACK_GROUND_IMAGE, FONT_PATH
from colors import LIGHT_BROWN, SUPER_LIGHT_GREEN, WHITE
from funtions import get_font
from class_button import Button
from controller_game import controller_play_game
from controller_option import controller_options_menu

def controller_main_menu():
    while True:
        WINDOW.blit(BACK_GROUND_IMAGE, (0, 0))

        mouse_position_main_menu = pygame.mouse.get_pos()

        MAIN_MENU_TEXT = get_font(FONT_PATH, 100).render("MAIN MENU", True, LIGHT_BROWN)
        MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(pygame.image.load(r"assets\Play Rect.png"), 640, 250, "PLAY", get_font(FONT_PATH, 75), SUPER_LIGHT_GREEN, WHITE)
        OPTIONS_BUTTON = Button(pygame.image.load(r"assets\Options Rect.png"), 640, 400, "OPTIONS", get_font(FONT_PATH, 75), SUPER_LIGHT_GREEN, WHITE)
        QUIT_BUTTON = Button(pygame.image.load(r"assets\Quit Rect.png"), 640, 550, "QUIT", get_font(FONT_PATH, 75), SUPER_LIGHT_GREEN, WHITE)

        WINDOW.blit(MAIN_MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_position_main_menu)
            button.update(WINDOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_position_main_menu):
                    controller_play_game()
                if OPTIONS_BUTTON.checkForInput(mouse_position_main_menu):
                    controller_options_menu()
                if QUIT_BUTTON.checkForInput(mouse_position_main_menu):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()