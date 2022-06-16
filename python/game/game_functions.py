import sys
import pygame


def check_events():
    # respond to  keyboard and mouse item
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, net):
    # fill color
    screen.fill(ai_settings.bg_color)
    net.update()
    # visualiaze the window
    pygame.display.flip()
