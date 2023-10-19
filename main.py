import os
import random
import math
import pygame

from pygame.sprite import Group
from constants import WIDTH, HEIGHT, FPS
from funtions import get_background, handle_move, draw, load_sprite_sheets
from classes import Player

pygame.init()

pygame.display.set_caption("Juego en desarrollo...")

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    player = Player(100, 100, 50, 50, load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True))

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)
    
    pygame.quit()
    quit()

if __name__  == "__main__":
    main(window)