import sys
import pygame
import time
from settings import Settings
import hetu_functions as hf
from hetu import hetu


def run_game():
    # initialize game and create a dispaly object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Hetu")
    # set backgroud color
    bg_color = (settings.bg_color)

    ht = hetu(screen)

    # game loop
    while True:
        # supervise keyboard and mouse item
        hf.check_events()
        hf.update_screen(settings, screen, ht, 1)
        # time.sleep(0.3)


run_game()
