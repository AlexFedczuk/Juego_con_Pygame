import pygame

from constants import *
from colors import WHITE, BLACK, GREEN
from funtions import get_font

from class_button import Button_Text

def controller_options_menu():
    pygame.display.set_caption(NAME_GAME + " - Pause Menu")
    
    running = True
    while running:
            options_mouse_position = pygame.mouse.get_pos()

            WINDOW.fill(WHITE)

            OPTIONS_TEXT_FONT = get_font(FONT_PATH, NORMAL_SIZE_FONT).render("This is the OPTIONS screen.", True, BLACK)
            OPTIONS_RECT = OPTIONS_TEXT_FONT.get_rect(center=(WIDTH/2, 260))
            WINDOW.blit(OPTIONS_TEXT_FONT, OPTIONS_RECT)

            OPTIONS_BACK_BUTTON = Button_Text(None, WIDTH/2, HEIGHT/1.7, "BACK", get_font(FONT_PATH, NORMAL_SIZE_FONT), BLACK, GREEN)

            OPTIONS_BACK_BUTTON.change_color(options_mouse_position)
            OPTIONS_BACK_BUTTON.update(WINDOW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Cerrando juego.")
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if OPTIONS_BACK_BUTTON.check_input(options_mouse_position):
                        running = False
            pygame.display.update()