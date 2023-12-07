import pygame
from settings import Settings
from plane import c_plane
from fan import c_fan


class entity():
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.centerx = screen.get_rect().centerx
        self.centery = screen.get_rect().centery

        self.lst_entity: list = []

        self.lst_entity.append(c_plane(
            [self.centerx, self.centery], 90))
        self.lst_entity.append(c_plane(
            [self.centerx, self.centery], 45))
        
    def update(self):
        pass

    def draw(self):
        for draw in self.lst_entity:
            pygame.draw.polygon(
                self.screen, self.settings.black_color, draw.auto_move(), 1)
