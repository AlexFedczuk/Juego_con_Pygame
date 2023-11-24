import pygame

from constants import WINDOW, BACK_GROUND_IMAGE, FONT_PATH, WIDTH
from colors import LIGHT_BROWN, SUPER_LIGHT_GREEN, WHITE
from funtions import get_font
from class_button import Button
from controller_game import controller_play_game
from controller_option import controller_options_menu

def controller_main_menu():
    running = True
    while running:
        pygame.display.set_caption("Juego en desarrollo... - Menu principal")

        WINDOW.blit(BACK_GROUND_IMAGE, (0, 0))

        mouse_position_main_menu = pygame.mouse.get_pos()

        MAIN_MENU_TEXT = get_font(FONT_PATH, 50).render("MAIN MENU", True, LIGHT_BROWN)
        MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(WIDTH/2, 100))

        PLAY_BUTTON = Button(pygame.image.load(r"assets\Play Rect.png"), WIDTH/2, 250, "PLAY", get_font(FONT_PATH, 25), SUPER_LIGHT_GREEN, WHITE)
        OPTIONS_BUTTON = Button(pygame.image.load(r"assets\Options Rect.png"), WIDTH/2, 400, "OPTIONS", get_font(FONT_PATH, 25), SUPER_LIGHT_GREEN, WHITE)
        QUIT_BUTTON = Button(pygame.image.load(r"assets\Quit Rect.png"), WIDTH/2, 550, "QUIT", get_font(FONT_PATH, 25), SUPER_LIGHT_GREEN, WHITE)

        WINDOW.blit(MAIN_MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_position_main_menu)
            button.update(WINDOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_position_main_menu):
                    controller_play_game()
                if OPTIONS_BUTTON.checkForInput(mouse_position_main_menu):
                    controller_options_menu()
                if QUIT_BUTTON.checkForInput(mouse_position_main_menu):
                    print("Cerrando juego.")
                    running = False
        pygame.display.update()