import sys
import pygame
import time
from settings import Settings
from net import c_net
import game_functions as gf


def run_game():
    # initialize game and create a dispaly object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Net Game")
    # set backgroud color
    bg_color = (230, 230, 230)

    net = c_net(settings, screen)

    # game loop
    while True:
        # supervise keyboard and mouse item
        gf.check_events()
        gf.update_screen(settings, screen, net)
        time.sleep(1)


run_game()
