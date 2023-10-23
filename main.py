import os
import random
import math
import pygame

from pygame.sprite import Group
from constants import WIDTH, HEIGHT, FPS
from funtions import get_background, handle_move, draw, load_sprite_sheets, get_block
from classes import Player, Block

pygame.init()

pygame.display.set_caption("Juego en desarrollo...")

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    block_size = 96

    player = Player(100, 100, 50, 50, load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True))
    # blocks = [Block(0, HEIGHT - block_size, block_size, get_block)]
    floor = [Block(i * block_size, HEIGHT - block_size, block_size, get_block) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]

    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
        player.loop(FPS)
        handle_move(player, floor)
        draw(window, background, bg_image, player, floor, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
            (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
    
    pygame.quit()
    quit()

if __name__  == "__main__":
    main(window)