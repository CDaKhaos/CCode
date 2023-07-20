import pygame
import random
from shapely import ops
from shapely import geometry
from settings import Settings
from math import pi
from circle import c_circle
from ellipse import c_ellipse


class envelope():
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.centerx = screen.get_rect().centerx
        self.centery = screen.get_rect().centery

        self.__sml_radius: int = 30

        self.shape: list = []
        for i in range(3):
            self.__sml_radius += random.randint(-5, 5)
            self.shape.append(
                c_circle([self.centerx, self.centery], self.__sml_radius))

            ellipse_y = random.randint(0, 20) / 10 * self.__sml_radius
            self.shape.append(
                c_ellipse([self.centerx, self.centery], self.__sml_radius, ellipse_y))

    def update(self):
        pass

    def draw(self):
        # convert to geometry
        geoPolygons = []
        for shape in self.shape:
            geoPolygons.append(geometry.Polygon(shape.auto_move()))

        # calc union
        geoPoints = ops.unary_union(geoPolygons)
        if geoPoints.geom_type == 'MultiPolygon':
            for geos in list(geoPoints.geoms):
                self.draw_geoPloygon(geos)

        elif geoPoints.geom_type == 'Polygon':
            self.draw_geoPloygon(geoPoints)

        pass

    def draw_geoPloygon(self, geoPolygon):
        if geoPolygon.geom_type != 'Polygon':
            return

        # convert
        lst_draw = []
        lst_draw.append(geoPolygon.exterior.coords[:-1])

        # draw
        for draw in lst_draw:
            pygame.draw.polygon(
                self.screen, self.settings.black_color, draw, 1)
