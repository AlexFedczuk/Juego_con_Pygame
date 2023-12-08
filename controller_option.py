import pygame
from pygame import mixer

from constants import *
from colors import *
from funtions import *

from class_button import Button_Text
from class_slider import Slider

def controller_options_menu(mute_volume_flag:bool, volumen_value:float):
    pygame.display.set_caption(NAME_GAME + " - Pause Menu")

    SLIDER = Slider(500, 500, 300, 30, 0.1, 0, 100)
    
    running = True
    while running:
            if mute_volume_flag:
                color = "red"
            else:
                color = "green"
            options_mouse_position = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()

            WINDOW.blit(BACK_GROUND_IMAGE, ORIGIN_POINT)

            MAIN_MENU_TEXT = get_font(FONT_PATH, BIG_SIZE_FONT).render("OPTIOS MENU", True, LIGHT_BROWN)
            MENU_RECT = MAIN_MENU_TEXT.get_rect(center=(WIDTH/2, 100))
            WINDOW.blit(MAIN_MENU_TEXT, MENU_RECT)

            MUTE_VOLUME_BUTTON = Button_Text(pygame.image.load(PLAY_RECT_PATH), WIDTH/2, HEIGHT/2.1, "MUTE VOLUME", get_font(FONT_PATH, NORMAL_SIZE_FONT), color, color)
            GO_BACK_BUTTON = Button_Text(pygame.transform.scale(pygame.image.load(PLAY_RECT_PATH), (125, 70)), WIDTH/2, HEIGHT/1.2, "GO BACK", get_font(FONT_PATH, SMALL_SIZE_FONT), SUPER_LIGHT_GREEN, WHITE)

            for button in [MUTE_VOLUME_BUTTON, GO_BACK_BUTTON]:
                button.change_color(options_mouse_position)
                button.update(WINDOW)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Cerrando juego.")
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if MUTE_VOLUME_BUTTON.check_input(options_mouse_position):
                        mute_volume_flag = not mute_volume_flag
                    elif GO_BACK_BUTTON.check_input(options_mouse_position):
                        running = False         

            if SLIDER.container_rect.collidepoint(options_mouse_position) and mouse[0]:                   
                SLIDER.move_slider(options_mouse_position)
            SLIDER.render(WINDOW)
            volumen_value = control_sound(mute_volume_flag, SLIDER.get_value())
            pygame.display.update()
    return [mute_volume_flag, volumen_value]