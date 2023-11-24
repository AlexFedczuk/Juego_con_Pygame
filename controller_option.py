import pygame, sys

from constants import WINDOW, FONT_PATH
from colors import WHITE, BLACK
from funtions import get_font
from class_button import Button

def controller_options_menu():
    running = True
    while running:
            options_mouse_position = pygame.mouse.get_pos()

            WINDOW.fill(WHITE)

            OPTIONS_TEXT_FONT = get_font(FONT_PATH, 45).render("This is the OPTIONS screen.", True, BLACK)
            OPTIONS_RECT = OPTIONS_TEXT_FONT.get_rect(center=(640, 260))
            WINDOW.blit(OPTIONS_TEXT_FONT, OPTIONS_RECT)

            OPTIONS_BACK_BUTTON = Button(None, 640, 460, "BACK", get_font(FONT_PATH, 75), BLACK, "Green")

            OPTIONS_BACK_BUTTON.changeColor(options_mouse_position)
            OPTIONS_BACK_BUTTON.update(WINDOW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK_BUTTON.checkForInput(options_mouse_position):
                        running = False
            pygame.display.update()