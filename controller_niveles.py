import pygame

from constants import *
from colors import WHITE, LIGHT_BROWN, SUPER_LIGHT_GREEN
from funtions import get_font

from class_button import Button_Text
from controller_game import controller_play_game

def controller_levels_menu():
    pygame.display.set_caption(NAME_GAME + " - Pause Menu")

    running = True
    while running:
        WINDOW.blit(BACK_GROUND_IMAGE, ORIGIN_POINT)

        mouse_position = pygame.mouse.get_pos()

        MAIN_MENU_TEXT = get_font(FONT_PATH, BIG_SIZE_FONT).render("LEVELS", True, LIGHT_BROWN)
        MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(WIDTH/2, 100))

        LEVEL_ONE = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/3.5, "LEVEL 1", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        LEVEL_TWO = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/2.1, "LEVEL 2", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        LEVEL_THREE = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/1.5, "LEVEL 3", get_font(FONT_PATH, NORMAL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        GO_BACK_BUTTON = Button_Text(pygame.transform.scale(pygame.image.load(PLAY_RECT_PATH), (125, 70)), WIDTH/2, HEIGHT/1.2, "GO BACK", get_font(FONT_PATH, SMALL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)
        WINDOW.blit(MAIN_MENU_TEXT, MENU_RECT)

        for button in [LEVEL_ONE, LEVEL_TWO, LEVEL_THREE, GO_BACK_BUTTON]:
            button.change_color(mouse_position)
            button.update(WINDOW)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Cerrando juego.")
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if LEVEL_ONE.check_input(mouse_position):
                    controller_play_game()
                elif LEVEL_TWO.check_input(mouse_position):
                    controller_play_game()
                elif LEVEL_THREE.check_input(mouse_position):
                    controller_play_game()
                elif LEVEL_THREE.check_input(mouse_position):
                    controller_play_game()
                elif GO_BACK_BUTTON.check_input(mouse_position):
                    running = False
        pygame.display.update()